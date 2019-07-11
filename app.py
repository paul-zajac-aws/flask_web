# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Flask, goodbye'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
