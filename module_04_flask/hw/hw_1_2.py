"""
В /registration endpoint добавьте все валидаторы,
о которых говорилось на последнем уроке:
    1) email (обязательно для заполнение, валидация формата),
    2) phone (обязательно для заполнения, длина 10 символов, только числа),
    3) name (обязательно для заполнения),
    4) address (обязательно для заполнения),
    5) index (только числа, обязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,validators,ValidationError
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)




class RegistrationForm(FlaskForm):
    email = StringField(validators=[validators.InputRequired(),validators.Email()])

    phone = IntegerField(validators=[validators.InputRequired()])
    def validate_phone(form, field):
        if len(str(field.data)) != 10:
            raise ValidationError('phone must be 10 characters')
    #Числа он сам валидирует за счет поля integer

    name = StringField(validators=[validators.InputRequired()])
    address = StringField(validators=[validators.InputRequired()])
    index = IntegerField(validators=[validators.InputRequired()])

    def validate_index(form, field):
        if type(field.data) != int:
            raise ValidationError('must be int')

    # Числа он сам валидирует за счет поля integer
    comment = StringField(validators=[validators.InputRequired()])




@app.route("/registration", methods=["POST","GET"])
def registration():

    form = RegistrationForm()
    phone=form.phone.data

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors},{phone}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
    app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
