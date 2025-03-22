from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# This is a simple Flask application that returns "Hello, DevOps World!" when accessed at the root URL.
# It is designed to be run in a Docker container, which is specified in the Dockerfile.