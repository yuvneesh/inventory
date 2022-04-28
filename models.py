from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

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
    ProductID = db.Column(db.String, primary_key = True)
    Vendor = db.Column(db.String, ForeignKey('vendors.VendorID'))
    CatalogNumber = db.Column(db.String, nullable=False)

class Certificates(db.Model):
    CertificateID = db.Column(db.String, primary_key=True)
    Product = db.Column(db.String,ForeignKey('products.ProductID'))
    CertificationDate = db.Column(db.Date)
    ExpiryDate = db.Column(db.Date)

class Log(db.Model):
    SerialNumber = db.Column(db.Integer, primary_key=True)
    Product = db.Column(ForeignKey('products.ProductID'))
    LotNumber = db.Column(db.String,nullable=False)
    
    DateReceived = db.Column(db.Date,nullable=False)
    ReceivedBy = db.Column(db.String,nullable=False)
    Certificate = db.Column(db.Boolean,nullable=False)

    DateWithdrawn = db.Column(db.Date,nullable=False)
    WithdrawnBy = db.Column(db.String,nullable=False)

    DateDisposed = db.Column(db.Date,nullable=False)
    DisposedBy = db.Column(db.String,nullable=False)

class Inventory(db.Model):
    Product = db.Column(ForeignKey('products.ProductID'),primary_key=True)
    Stock = db.Column(db.Integer)

