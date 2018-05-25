from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return '<h1>admin Page</h1>'


@app.route('/user/<name>')
def user_name(name):
    return '<h1>hello % s</h1>' % name


if __name__ == '__main__':
    app.run(port=8080)
