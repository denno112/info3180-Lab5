# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    desc = TextAreaField("Description", validators=[InputRequired()])
    poster = FileField("Poster", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])