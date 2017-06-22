# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9003,debug=True)