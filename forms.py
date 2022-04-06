from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField

class AddForm(FlaskForm):
    Product = SelectField(label='Product',choices=['','TAN3','TBN6'])
    LotNo = StringField('Lot No:')