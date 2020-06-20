#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(param1=None):
    return 'Hello, World! Param1: ' + str(param1)

@app.route('/article/<newone>')
def article(param1=None,newone=None):
    return 'This is article. Param1: ' + str(param1)  + " newpath: " + str(newone)

