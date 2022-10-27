#!/usr/bin/env python3
import http.server
import socketserver
import os
from time import strftime, time

#print('source code for "http.server":', http.server.__file__)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
