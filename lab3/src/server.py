#!/usr/bin/env python3
import http.server
import socketserver
import os
from time import strftime, time
from flask import Flask, request

app = Flask(__name__)


def analyze_str(param_str: str):
    res_str = {"lowercase": 0, "uppercase": 0, "digits": 0, "special": 0}
    return res_str


@app.route("/")
def hello_world():
    str_param = request.args.get('str', type=str)

    return analyze_str(str_param)


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
