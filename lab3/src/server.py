#!/usr/bin/env python3
import http.server
import socketserver
import os
from time import strftime, time
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    str_param = request.args.get('str', type=str)
    return "<p>" + str(str_param) + "</p>"


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
