from flask import flask
app = Flask(__name__)

@app.route('/')
def response():
    return "Hello World from a Flask container!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
