from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import DateField
from wtforms import SubmitField

class AddForm(FlaskForm):
    Product = SelectField(label='Product',choices=['','TAN3','TBN6'])
    LotNo = StringField('Lot No')
    RecdDate = DateField('Received Date')
    RecdInit = StringField('Received By')
    submit = SubmitField("Submit")
    
    