#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return render_template('user_input.html', input_text=input_text)

    
    # return "You entered: " + input_text