from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    content = TextAreaField('Text', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')