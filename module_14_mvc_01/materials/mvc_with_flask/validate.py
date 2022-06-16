from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,validators,ValidationError

class BookForm(FlaskForm):
    title = StringField(validators=[validators.InputRequired()])

    author = StringField(validators=[validators.InputRequired()])