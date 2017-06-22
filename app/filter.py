# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask.ext.babel import Babel
from flask.ext.babel import format_datetime


babel = Babel()


def my_format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return format_datetime(value, format)