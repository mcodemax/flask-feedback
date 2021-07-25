from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, ValidationError, URL, AnyOf
from models import MAX_NOTE_LEN, MAX_USERNAME_LEN, MAX_TITLE_LEN, MAX_EMAIL_LEN, MAX_NAME_LEN

class AddUserForm(FlaskForm):
    """Form for adding Users"""

    username = StringField("Username", 
                        validators=[InputRequired(), Length(min=1, max=MAX_NAME_LEN)])
                                
    password = PasswordField("Password", 
                        validators=[InputRequired(), Length(min=1)])  

    email = StringField("Email", 
                        validators=[InputRequired(), Length(min=1, max=MAX_EMAIL_LEN)])

    first_name = StringField("First Name", 
                        validators=[InputRequired(), Length(min=1, max=MAX_NAME_LEN)])

    last_name = StringField("Last Name", 
                        validators=[InputRequired(), Length(min=1, max=MAX_NAME_LEN)])

