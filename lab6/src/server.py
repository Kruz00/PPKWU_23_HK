#!/usr/bin/env python3
from flask import Flask, request, Response
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml

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
    json_response = {}
    root = ET.fromstring(request.data)
    num1 = None
    num2 = None

    if "str" == root.tag:
        json_response.update(analyze_str(root.text))
    else:
        for child in root:
            if "str" == child.tag:
                json_response.update(analyze_str(child.text))
            if "num1" == child.tag:
                num1 = int(child.text)
            if "num2" == child.tag:
                num2 = int(child.text)
    if num1 is not None and num2 is not None:
        json_response.update(calculate(num1, num2))

    response_xml = dicttoxml(json_response, attr_type=False)
    r = Response(response=response_xml, status=200, mimetype="application/xml")
    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r


# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')
