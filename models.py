from sqlalchemy import ForeignKey
from inventory import db

class TestMethods(db.Model):
    MethodID = db.Column(db.String, primary_key=True)
    MethodName = db.Column(db.String, nullable=False)

class Link_test_products(db.Model):
    LinkID = db.Column(db.Integer,primary_key=True)
    Method = db.Column(ForeignKey('test_methods.MethodID'))
    Product = db.Column(ForeignKey('products.ProductID'))

class Vendors(db.Model):
    VendorID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    VendorName = db.Column(db.String, nullable=False)
    products = db.relationship('Products', backref="vendor", lazy=True)

class Products(db.Model):
    ProductID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    ProductName = db.Column(db.String,nullable=False)
    Vendor = db.Column(db.String, ForeignKey('vendors.VendorID'))
    CatalogNumber = db.Column(db.String, nullable=False)

class Certificates(db.Model):
    CertificateID = db.Column(db.String, primary_key=True)
    Product = db.Column(db.String,ForeignKey('products.ProductID'))
    CertificationDate = db.Column(db.Date)
    ExpiryDate = db.Column(db.Date)

class Log(db.Model):
    SerialNumber = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Product = db.Column(ForeignKey('products.ProductID'))
    LotNumber = db.Column(db.String,nullable=False)
    
    ReceivedBy = db.Column(db.String)
    Certificate = db.Column(db.Boolean)
    DateReceived = db.Column(db.Date)

    DateWithdrawn = db.Column(db.Date)
    WithdrawnBy = db.Column(db.String)

    DateDisposed = db.Column(db.Date)
    DisposedBy = db.Column(db.String)

class Inventory(db.Model):
    Product = db.Column(ForeignKey('products.ProductID'),primary_key=True)
    Stock = db.Column(db.Integer)

