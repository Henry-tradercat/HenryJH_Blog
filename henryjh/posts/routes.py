from flask import render_template, Blueprint, redirect, url_for, flash, request, flash
from flask_login import login_required, current_user
from henryjh.models import Post, Category
from henryjh.posts.forms import PostForm
from henryjh import db


posts = Blueprint('posts', __name__)


@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/posts", methods=['GET', 'POST'])
def post_pages():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('posts.html', title='Posts', posts=posts)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        select_category = request.form['category']
        category = Category.query.filter_by(category_name=select_category).first()
        post = Post(title=form.title.data, content=form.content.data, category_id=category.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has beend created!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    return render_template('create_post.html', title='New Post', form=form, categories=categories, legend='New Post')

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', 
                            form=form, categories=categories, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been delete!', 'success')
    return redirect(url_for('posts.post_pages'))




    