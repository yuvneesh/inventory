from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class ReceiveForm(FlaskForm):
    name = "Receiving Form"
    ProductName = SelectField(label='Product', validators=[DataRequired()])
    LotNumber = StringField('Lot No',validators=[DataRequired()])
    DateReceived = DateField('Received Date', validators=[DataRequired()])
    ReceivedBy = StringField('Received By', validators=[DataRequired()])
    Certificate = SelectField(label='Certificate',
                              choices=['Yes','No'])
    submit = SubmitField('Submit')
    
class WithdrawForm(FlaskForm):
    name = "Withdrawing Form"
    ProductName = SelectField('Product', validators=[DataRequired()])
    SerialNumber = SelectField('Available item number', validate_choice=False, validators=[DataRequired()])
    DateWithdrawn = DateField('Date of withdrawl', validators=[DataRequired()])
    WithdrawnBy = StringField('Technician Initials', validators=[DataRequired()])
    Withdraw = SubmitField('Withdraw')
    Certificate = SubmitField('Get Certificate')

class DisposeForm(FlaskForm):
    name = "Dispose Form"
    ProductName = SelectField('Product', validators=[DataRequired()])
    SerialNumber = StringField('Item Number to dispose', validators=[DataRequired()])
    DateDisposed = DateField('Date of disposal', validators=[DataRequired()])
    DisposedBy = StringField('Technician Initials', validators=[DataRequired()])
    Dispose = SubmitField('Dispose')


class AddProducts(FlaskForm):
    name = "New Product Form"
    ProductName = StringField("Product",
                              validators=[DataRequired()])
    CatalogNumber = StringField("Catalog Number",
                                validators=[DataRequired()])
    VendorID = StringField("VendorID",
                           validators=[DataRequired()])
    add = SubmitField('Add')

class AddVendors(FlaskForm):
    name = "Add Vendors"
    VendorName = StringField("Vendor Name",
                             validators=[DataRequired()])
    add = SubmitField('Add')