from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class EditProfile(FlaskForm):

    username = StringField('Username:')
    email = EmailField('E-mail')
    image_url= StringField('Image_url:')
    header_image_url= StringField('header_image_url')
    bio = TextAreaField('Biography:')
    password= PasswordField('Password', validators=[InputRequired()])