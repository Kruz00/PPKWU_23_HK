#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)


def calculate(num1: int, num2: int):
    _sum = int(num1) + int(num2)
    _sub = int(num1) - int(num2)
    _mul = int(num1) * int(num2)
    _div = int(num1) // int(num2)
    _mod = int(num1) % int(num2)

    res_str = {
        "sum": _sum,
        "sub": _sub,
        "mul": _mul,
        "div": _div,
        "mod": _mod
    }
    return res_str


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


@app.route("/", methods=['POST'])
def handle_post_request():
    json_request = request.json
    json_response = {}
    if "str" in json_request:
        json_response.update(analyze_str(json_request["str"]))
    if "num1" in json_request and "num2" in json_request:
        json_response.update(calculate(json_request["num1"], json_request["num2"]))

    return json_response


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
# done
