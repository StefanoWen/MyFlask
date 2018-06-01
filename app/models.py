# -*- coding:utf-8 -*-
import bleach

from config import db
from datetime import datetime
from markdown import markdown

# # 如果SQL是insert之类的DML语句，要记得commit：
# conn.commit()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:toor@127.0.0.1:3306/flask_db?charset=utf8')
DB_Session = sessionmaker(bind=engine)
db_session = DB_Session()


class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    user_id = db.relationship('Article', backref='User', lazy='dynamic')


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text, nullable=False)
    data_publish = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content_html = db.Column(db.Text)

    @staticmethod
    def on_content_change(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'ul', 'strong', 'p', 'h1', 'h2', 'h3']
        content_html = markdown(value, output_format='html')
        content_html = bleach.clean(content_html, tags=allowed_tags, strip=True)
        content_html = bleach.linkify(content_html)
        target.content_html = content_html


db.event.listen(Article.content, 'set', Article.on_content_change)
