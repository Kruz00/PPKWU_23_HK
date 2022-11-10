#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)


def analyze_str(param_str: str):
    lowercase = sum(1 for c in param_str if c.islower())
    uppercase = sum(1 for c in param_str if c.isupper())
    digits = sum(1 for c in param_str if c.isdigit())
    special = len(param_str) - sum([lowercase, uppercase, digits])
    res_str = {"lowercase": lowercase,
               "uppercase": uppercase,
               "digits": digits,
               "special": special}
    return res_str


@app.route("/")
def hello_world():
    str_param = request.args.get('str', type=str)

    return analyze_str(str_param)


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
