# -*- coding:utf-8 -*-
from flask import Flask
# from config import app

app = Flask(__name__)
app.config.from_object('config')
from app import models, views
