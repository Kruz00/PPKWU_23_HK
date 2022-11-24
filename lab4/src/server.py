#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)


def calculate(num1: int, num2: int):

    res_str = {"sum": 0,
               "sub": 0,
               "mul": 0,
               "div": 0,
               "mod": 0
               }
    return res_str


@app.route("/")
def hello_world():
    num1_param = request.args.get('num1', type=int)
    num2_param = request.args.get('num2', type=int)
    return calculate(num1_param, num2_param)


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
