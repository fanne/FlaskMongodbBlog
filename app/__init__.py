# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask import Flask

from views import bp
from models import db
from admin import create_admin
from flask.ext.login import LoginManager
#from flask.ext.babel import Babel
from filter import babel,my_format_datetime
from upload import uploadfile


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    register_babel(app)
    register_jinjia_filters(app)
    register_blueprints(app)
    register_database(app)



    create_admin(app)
    init_login(app)
    return app

def register_blueprints(app):
    app.register_blueprint(bp)
    app.register_blueprint(uploadfile)


def register_database(app):
    db.init_app(app)

def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.objects(id=user_id).first()

def register_babel(app):
    babel.init_app(app)


def register_jinjia_filters(app):
    app.jinja_env.filters['my_format_datetime'] = my_format_datetime




