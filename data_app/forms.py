try:
    from flask_wtf import FlaskForm
    from wtforms.validators import DataRequired, Email
    from wtforms import StringField, SubmitField
    import email_validator
except ModuleNotFoundError:
    print('module not found')


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Login')
