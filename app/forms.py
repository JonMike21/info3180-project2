# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, DateField, EmailField,PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import  FileRequired, FileAllowed

class UserForm(FlaskForm):
    username= StringField('Username', validators=[InputRequired()])
    password= StringField('Password', validators=[InputRequired()])
    firstname= StringField('Firstname', validators=[InputRequired()])
    lastname= StringField('Lastname', validators=[InputRequired()])
    email= EmailField('Email', validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profile_photo = FileField('Profile_photo', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg','JPG'], 'Images only!')])    
    #joined_on = DateField('Joined_on', format='%m/%d/%Y', validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class PostForm(FlaskForm):
    caption = TextAreaField('Caption', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg','JPG'], 'Images only!')]) 