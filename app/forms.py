from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    desc = TextAreaField('Description', validators=[InputRequired()])
    numOfBed = StringField('No. of Rooms', validators=[InputRequired()])
    numOfBath = StringField('No. of Bathrooms', validators=[InputRequired()])
    pric = StringField('Price', validators=[InputRequired()])
    proptype = SelectField('Property Type',choices=[('House', 'House'), ('Apartment','Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    pic= FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],'Images only')])