from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    title = StringField('Category')
    content = SelectField('Content')
    add_text = StringField('Add_text')
    add = SubmitField('Add')
    remove = SubmitField('Remove')
    