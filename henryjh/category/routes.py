from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from henryjh.models import Category
from henryjh.category.forms import CategoryForm
from henryjh import db

category = Blueprint('category', __name__)


@category.route("/categories", methods=['GET', 'POST'])
@login_required
def categories():
    form = CategoryForm()
    datas = Category.query.all()
    if request.method == 'POST':
        if form.add.data:
            if request.form['add_text'] != '':
                select = request.form['add_text']
                new_category = Category(category_name=select)
                db.session.add(new_category)
                db.session.commit()
                return redirect(url_for('category.categories'))
        elif form.remove.data:
            try:
                select = request.form['custom-select']
                old_category = Category.query.filter_by(category_name=str(select)).first()
                db.session.delete(old_category)
                db.session.commit()
            except:
                pass
        return redirect(url_for('category.categories'))
    return render_template('category.html', title='Category', form=form, datas=datas)

