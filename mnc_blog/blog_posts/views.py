from flask import render_template,redirect,flash,url_for,Blueprint,request
from mnc_blog import db
from mnc_blog.models import BlogPost
from flask_login import current_user,login_required
from mnc_blog.blog_posts.forms import BlogPostForm

blog_posts=Blueprint('blog_posts',__name__)

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create():

    form=BlogPostForm()

    if form.validate_on_submit():
        blog_post=BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('create_post.html',form=form)

@blog_posts.route('/<int:blog_post_id>')
def read(blog_post_id):
    blog=BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog.title,date=blog.date,post=blog)

@blog_posts.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog=BlogPost.query.get_or_404(blog_post_id)

    if blog.author != current_user:
        abort(403)

    form=BlogPostForm()

    if form.validate_on_submit():

        blog.title=form.title.data
        blog.text=form.text.data
        db.session.commit()
        return redirect(url_for('blog_posts.read',blog_post_id=blog_post_id))

    elif request.method=="GET":
        form.title.data=blog.title
        form.text.data=blog.text

    return render_template('create_post.html',title="Updating",form=form)

@blog_posts.route('/<int:blog_post_id>/delete',methods=['POST'])
@login_required
def delete(blog_post_id):
    blog=BlogPost.query.get_or_404(blog_post_id)

    if blog.author != current_user:
        abort(403)

    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('core.index'))