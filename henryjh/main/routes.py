from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_required
from henryjh.main.forms import UpdateAccountForm
from henryjh.models import About
from henryjh import db
from henryjh.main.utils import save_picture, delete_picture

main = Blueprint('main', __name__)

@main.route("/home")
@main.route("/")
def home():
    return render_template('home.html')


@main.route("/update_about", methods=['GET', 'POST'])
@login_required
def update_about():
    about = About.query.filter_by(id=1).first()
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            delete_picture()
            picture_file = save_picture(form.picture.data)
            about.image_file = picture_file
        about.name = form.name.data
        about.content = form.content.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.name.data = about.name
        form.content.data = about.content
    return render_template('about_me.html', form=form)

