# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask_admin import Admin
from view import MyIndexView,UserView,PostView
from ..models import User,Post
#from flask_admin.contrib.pymongo import ModelView
# from ..import db

def create_admin(app=None):
    admin = Admin(app, name="CleanBlogAdmin", index_view=MyIndexView(), base_template='admin/my_master.html')
    admin.add_view(UserView(User))
    admin.add_view(PostView(Post))

    # admin.add_view(ModelView(User,db.session))
