# rate-limiter
Implementation of a Web Application with a rate limiter which limits the amount of requests received from a single IP address 

## introduction
In this project, I have implemented a Web Application with a rate limiter which limits the amount of requests received from a single IP address to 15 per minute.

The code was written in Python, using Flask and Redis

## prerequisite
If you want to run the code you have 2 options:

1)Just go to http://3.122.112.199/whoami , the code is running on this server.

2)You can run the code on your local computer. to do so, you most have:

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
  <img src="https://github.com/eladshamailov/Assignment1/blob/master/programFlow.jpg?raw=true" width="600" height = "450"/>
</p>

