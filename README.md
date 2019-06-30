# Rate Limiter
Implementation of a Web Application with a rate limiter which limits the amount of requests received from a single IP address.

## Introduction
In this project, I have implemented a Web Application with a rate limiter which limits the amount of requests received from a single IP address to 15 per minute.

The code was written in Python, using Flask and Redis.

The Implementation is in the file named: rate-limiter.py

## Prerequisite
If you want to run the code you have 2 options:

1) Just go to http://3.122.112.199/whoami , the code is running on this server (Using AWS lightsail).

2) You can run the code on your local computer. to do so, you most have:

* Python installed on your computer.
* Redis server installed on your computer.
* Flask installed on your computer.
In the instructions section below, you can find a full guide on how to do it.

## Instructions 
First of all, please make sure you have Python installed.

The next step in to install Flask.

To install Flask, please write:
```
pip install Flask
```
If you want to work with the latest Flask code before it’s released, install or update the code from the master branch:

```
pip install -U https://github.com/pallets/flask/archive/master.tar.gz
```

Now, Let's install Redis.

You can find a great guide here: https://redis.io/topics/quickstart

You can also follow those lines:
```
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get install redis-server
> redis-cli -v
```
To stop your Redis server:
```
> sudo service redis-server stop
```

## Running the code
After you have installed Python, Flask and redis you can run the program.

To do so:
1) Download the rate-limiter.py and place it in a new folder
2) Make sure that the Redis server is up and running
3) Excetue the rate-limiter.py file. 
```
Python rate-limiter.py
```
4) You should see something like this:
<p align="left">
  <img src="https://github.com/eladshamailov/rate-limiter/blob/master/InAppExample.PNG"/>
</p>

5) Now, Please go to:
http://127.0.0.1:5000/whoami
The code is running there.

6) A valid response will look like this:

<p align="left">
  <img src="https://github.com/eladshamailov/rate-limiter/blob/master/ValidResponseBrower.PNG"/>
</p>
With status code 200

<p align="left">
  <img src="https://github.com/eladshamailov/rate-limiter/blob/master/ValidCode.PNG"/>
</p>

7) After you have reached the limit, you will get a response like this:

<p align="left">
  <img src="https://github.com/eladshamailov/rate-limiter/blob/master/InvalidAccess.PNG"/>
</p>
with status code 500

<p align="left">
  <img src="https://github.com/eladshamailov/rate-limiter/blob/master/InvalidStatus.PNG"/>
</p>

8) If you want to make a public endpoint , you can use ngrok.

You can download it from here: https://dashboard.ngrok.com/get-started

Follow the guide on the link, and then just execute:
```
ngrok http 5000
```
Now you will get a link, 
just follow this link and add 
```
/whoami
```
to the url.

## References
* For the integration of Flask and Redis, I've used this article found on Flask's site:

http://flask.pocoo.org/snippets/70/

* For deploying Flask to AWS, I've used this guide:
https://www.matthealy.com.au/blog/post/deploying-flask-to-amazon-web-services-ec2/

* For creating a secret key, I've used this article found on Flask's site:
http://flask.pocoo.org/docs/1.0/quickstart/
