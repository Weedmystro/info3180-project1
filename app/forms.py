
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed



class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators = [DataRequired()])
    bedrooms = IntegerField('No.of Rooms', validators = [DataRequired()])
    baths = IntegerField('No.of Bathrooms', validator = [DataRequired()])
    pType = SelectField('Property Type', choices = [("None", "Select Type"), [('House', 'House'), ('Apartment', 'Apartment')], validators = [DataRequired()])
    location=StringField('Location',validators=[DataRequired()])
    price = FloatField('Price',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    image = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])