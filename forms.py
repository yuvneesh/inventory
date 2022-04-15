from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import DateField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class ReceiveForm(FlaskForm):
    Product = SelectField(label='Product',choices=['','TAN3','TBN6'])
    LotNo = StringField('Lot No')
    RecdDate = DateField('Received Date')
    RecdInit = StringField('Received By')
    submit = SubmitField('Submit')
    
class WithdrawForm(FlaskForm):
    Product = SelectField(label='Product',choices=['','TAN3','TBN6'])
    AvailableItem = StringField('Available item number')
    WithdrawlDate = DateField('Date of withdrawl')
    WithdrawlTech = StringField('Technician Initials')
    Withdraw = SubmitField('Withdraw')
    Certificate = SubmitField('Get Certificate')

class AddMaterials(FlaskForm):
    Product = StringField("Product",validators=[DataRequired()])
    CatalogNumber = StringField("Catalog Number",validators=[DataRequired()])
    add = SubmitField('Add')
