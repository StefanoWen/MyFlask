from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/admin')
def admin():
    return 'admin page'


@app.route('/UA')
def UA():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is % s</p>' % user_agent


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
