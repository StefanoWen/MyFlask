# -*- coding:utf-8 -*-
from app import app
from flask import render_template, request, flash, redirect, url_for
from models import db_session
from hashlib import md5
from time import sleep


@app.route('/')
@app.route('/index/')
def hello_world():
    title = ''
    return render_template('index.html', title=title)


@app.route('/login/', methods=['GET'])
def login_form():
    title = u'登录'
    return render_template('login.html', title=title)


@app.route('/login/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    sql = db_session.execute('select username, password from user')
    data = sql.fetchone()
    if (username, md5(password).hexdigest()) == (data[0], data[1]):
        # title = u'登录成功'
        db_session.close()
        sleep(1)
        return redirect(url_for('hello_world'))  # render_template('login.html', title=title)
    else:
        title = u'登录失败'
        db_session.close()
        return render_template('login.html', title=title)


@app.route('/register/', methods=['GET'])
def register_form():
    title = u'注册'
    return render_template('register.html', title=title)


@app.route('/a/')
def a():
    return render_template('a.html')


@app.route('/b/')
def b():
    return render_template('b.html')


@app.route('/home/')
def home():
    return render_template('home.html')
