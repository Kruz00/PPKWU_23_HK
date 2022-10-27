#!/usr/bin/env python3
import http.server
import socketserver
import os
from time import strftime, time
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    cmd_param = request.args.get('cmd', type=str)
    str_param = request.args.get('str', type=str)
    if str(cmd_param) == "time":
        return "<p>" + strftime("%H:%M:%S") + "</p>"
    if str(cmd_param) == "rev":
        return "<p>" + str(str_param)[::-1] + "</p>"

    return "<p>Hello World! " + str(cmd_param) + " " + str(str_param) + "\n" + "</p>"


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
