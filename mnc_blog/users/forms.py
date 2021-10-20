from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email,EqualTo
from flask_login import current_user
from mnc_blog.models import User

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')

class RegisterForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('conf_password',message="Password must match!")])
    conf_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('conf_password',message="Password must match!")])
    submit=SubmitField('Register')

    def check_email(self,email_val):
        if User.query.filter_by(email=self.email_val.data).first():
            raise ValidationError("This email is already registered")

    def check_username(self,uname_val):
        if User.query.filter_by(username=self.uname_val.data).first():
            raise ValidationError("This username is already registered")

class UpdateUserForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def check_email(self,email_val):
        if User.query.filter_by(email=self.email_val.data).first():
            raise ValidationError("This email is already registered")

    def check_username(self,uname_val):
        if User.query.filter_by(username=self.uname_val.data).first():
            raise ValidationError("This username is already registered")