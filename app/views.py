# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask import render_template,Blueprint,make_response,request,url_for
from models import Post,User


bp = Blueprint('blog',__name__)

@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    paginator = Post.objects.paginate(page=page,per_page=10)
    return render_template("index.html",paginator=paginator)

    # posts = Post.objects.all()
    # return render_template("index.html",posts=posts)

@bp.route('/posts/<string:post_id>')
def get_post(post_id):
    post = Post.objects(id=post_id).first()
    return render_template("post.html",post=post)


@bp.route('/about')
def about():
    #user = User.objects.first()
    return render_template("about.html")




