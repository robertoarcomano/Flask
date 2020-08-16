# Flask
Flask Tutorial

## Main script <a href=index.sh>index.sh</a>
```
#!/bin/bash

export FLASK_APP=index.py
flask run
```
## Routing script <a href=route.py>route.sh</a>
```
#!/usr/bin/python

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def root():
    username = request.args.get('username')
    ret = ""
    ret = ret + request.url
    ret += "<br>" + "root()"
    ret += "<br>" + "username: " + str(username)
    return ret


@app.route('/user/')
@app.route('/user/<op>')
def user(op=None):
    username = request.args.get('username')
    ret = ""
    ret = ret + request.url
    ret += "<br>" + "user()"
    ret += "<br>" + "op: " + str(op)
    ret += "<br>" + "username: " + str(username)
    return ret
```
## Tests using PyTest  <a href=test_route.py>test_route.py</a>
#### Code
```
#!/usr/bin/python
import subprocess
import time
import requests
import os

from pytest import fail


def root():
    response = requests.get("http://localhost:5000/")
    return response.content.decode('utf-8') == "http://localhost:5000/<br>root()<br>username: None"


def user():
    response = requests.get("http://localhost:5000/user/add?username=user1")
    return response.content.decode(
        'utf-8') == "http://localhost:5000/user/add?username=user1<br>user()<br>op: add<br>username: user1"


def test_flask():
    subprocess.Popen("./index.sh", shell=False)
    time.sleep(5)
    tests = [
        root(),
        user()
    ]
    os.system("killall flask")
    if not all(tests):
        fail("ok")
```
#### Test Output
```
Testing started at 00:07 ...
/usr/bin/python3.8 /snap/pycharm-community/207/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /home/berto/PycharmProjects/Flask/test_route.py
Launching pytest with arguments /home/berto/PycharmProjects/Flask/test_route.py in /home/berto/PycharmProjects/Flask

============================= test session starts ==============================
platform linux -- Python 3.8.2, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3.8
cachedir: .pytest_cache
rootdir: /home/berto/PycharmProjects/Flask
collecting ... collected 1 item

test_route.py::test_flask PASSED                                         [100%] * Serving Flask app "route.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Aug/2020 00:07:21] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/Aug/2020 00:07:21] "GET /user/add?username=user1 HTTP/1.1" 200 -


=============================== warnings summary ===============================
/usr/lib/python3/dist-packages/socks.py:58
  /usr/lib/python3/dist-packages/socks.py:58: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
    from collections import Callable

-- Docs: https://docs.pytest.org/en/stable/warnings.html
========================= 1 passed, 1 warning in 5.14s =========================
Terminated

Process finished with exit code 0
```