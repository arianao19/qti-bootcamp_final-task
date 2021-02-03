from flask import Flask, jsonify

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