#!/usr/bin/env python3
import http.server
import socketserver
import os
from time import strftime, time
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World! </p>"


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
