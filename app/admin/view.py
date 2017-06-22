# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask_admin import AdminIndexView,expose
from flask_admin.contrib.mongoengine  import ModelView
from wtforms import fields, widgets
from flask.ext.login import current_user,login_user,logout_user
from flask import url_for,redirect,request
from form import LoginForm
from ..models import User


class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login'))
        return super(MyIndexView,self).index()

    @expose('/login',methods=('GET','POST'))
    def login(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = form.get_user()
            login_user(user)
            redirect(url_for('.index'))
        self._template_args['form']=form
        return super(MyIndexView,self).index()

    @expose('/logout')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

class PostView(ModelView):
    column_display_pk = True
    form_overrides = dict(content=CKTextAreaField)
    create_template = 'admin/createpost.html'
    edit_template = 'admin/editpost.html'

    column_choices = {
        'status':[
            (0,'draft'),
            (1,'published')
        ]
    }

    column_filters = ('title',)
    column_searchable_list = ('content',)
    column_sortable_list = ('create_time','modify_time',)
    column_default_sort = ('create_time',True)

    def is_accessible(self):
        return current_user.is_authenticated()
