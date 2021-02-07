from flask import Flask, jsonify, render_template, request, Response, redirect, url_for
from flask_bootstrap import Bootstrap

# configuration
DEBUG = True


# instantiate
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return "This is an example app"

if __name__ == '__main__':
    app.run()