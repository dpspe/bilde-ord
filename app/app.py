from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world!"


@app.route('/prediction')
def object_detection():
    pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
