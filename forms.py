from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import DateField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class ReceiveForm(FlaskForm):
    Product = SelectField(label='Product',choices=[],coerce=int,validate_choice=True)
    LotNo = StringField('Lot No')
    RecdDate = DateField('Received Date')
    RecdInit = StringField('Received By')
    Certificate = SelectField(label='Certificate',choices=['','Yes','No'])
    submit = SubmitField('Submit')
    
class WithdrawForm(FlaskForm):
    Product = SelectField(label='Product',choices=['','TAN3','TBN6'])
    AvailableItem = StringField('Available item number')
    WithdrawlDate = DateField('Date of withdrawl')
    WithdrawlTech = StringField('Technician Initials')
    Withdraw = SubmitField('Withdraw')
    Certificate = SubmitField('Get Certificate')

class AddProducts(FlaskForm):
    ProductName = StringField("Product",validators=[DataRequired()])
    CatalogNumber = StringField("Catalog Number",validators=[DataRequired()])
    VendorID = StringField("VendorID",validators=[DataRequired()])
    add = SubmitField('Add')

class AddVendors(FlaskForm):
    VendorName = StringField("Vendor Name",validators=[DataRequired()])
    add = SubmitField('Add')