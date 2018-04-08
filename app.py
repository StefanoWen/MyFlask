from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/admin')
def admin():
    return 'admin page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
