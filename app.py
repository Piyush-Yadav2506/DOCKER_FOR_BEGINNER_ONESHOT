# flask app for Docker hello world

from flask import Flask
import os
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World from Docker"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)