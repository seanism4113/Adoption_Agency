from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm (FlaskForm):
    name = StringField('Name', validators =[InputRequired(message = "Name cannot be blank")])
    species = SelectField('Species', validators = [InputRequired()], choices = [('', ''),('dog', 'dog'), ('cat', 'cat'), ('porcupine', 'porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Invalid URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available', default = True)
