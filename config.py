from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import MySQLdb

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@115.159.122.222:3306/flask_db?charset=utf8'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)

CSRF_ENABLED = True

SECRET_KEY = 'you-will-never-guess'
