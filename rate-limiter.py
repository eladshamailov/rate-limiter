from redis import Redis
redis = Redis()

import time
from functools import update_wrapper
from flask import request, g
from flask import Flask, jsonify
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import HTTPException, default_exceptions,  Aborter


app = Flask(__name__)
abort = Aborter()

class RateLimit(object):

    # We give the key extra expiration_window seconds time to expire in redis so that
    # badly synchronized clocks between the workers and the redis server do not cause problems.
    expiration_window = 5

    def __init__(self, key_prefix, limit, per):
        self.reset = (int(time.time()) // per) * per + per
        self.key = key_prefix + str(self.reset)
        self.limit = limit
        self.per = per
        # we use a pipeline to make sure that we never increment a key without
        # also setting the key expiration in case an exception happens between those lines (ex: process is killed)
        p = redis.pipeline()
        p.incr(self.key)
        p.expireat(self.key, self.reset + self.expiration_window)
        self.current = min(p.execute()[0], limit)

    # how many remaining requests we have left
    remaining = property(lambda x: x.limit - x.current)
    # return true if we over the limit, false otherwise
    over_limit = property(lambda x: x.current >= x.limit)

def get_view_rate_limit():
    # retrieve _view_rate_limit from the g object in flask
    return getattr(g, '_view_rate_limit', None)

def on_over_limit(limit):
    abort(500)

def ratelimit(limit, per=60,
              over_limit=on_over_limit,
              # scope_func=lambda: request.remote_addr,
              scope_func=lambda: request.remote_addr,
              key_func=lambda: request.endpoint):
    def decorator(f):
        def rate_limited(*args, **kwargs):
            key = 'rate-limit/%s/%s/' % (key_func(), scope_func())
            rlimit = RateLimit(key, limit, per)
            g._view_rate_limit = rlimit
            if over_limit is not None and rlimit.over_limit:
                return over_limit(rlimit)
            return f(*args, **kwargs)
        return update_wrapper(rate_limited, f)
    return decorator

#limit is the num of the limit for each IP address
#per is the time interval, in seconds
@app.route('/whoami', methods = ['GET', 'POST', 'HEAD', 'PUT'])
@ratelimit(limit=15, per=60)
def index():
    limit = get_view_rate_limit()
    ip = request.remote_addr
    return jsonify({'response': 'This is a rate limit response',
                    'your ip is:': '{}'.format(ip),
                    'limit:': '{}'.format(limit.limit),
                    'remaining access:': '{}'.format(limit.remaining),
                    'code:': '{}'.format(200),
                    'current access:': '{}'.format(limit.current)})

if __name__ == '__main__':
    # generate a secret key as described in the flask documentation
    app.secret_key = os.urandom(64)
    #we want to get the real IP in a safe way
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)