#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<hello>')
def print_string(hello):
    print(f"{hello}")
    return f"{hello}"

@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = '\n'.join(map(str, range(parameter)))
    return numbers.replace('\n', '<br>')

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
