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
