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
