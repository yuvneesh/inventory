from flask import Flask, render_template
import sqlalchemy
from forms import AddVendors, ReceiveForm, WithdrawForm, AddProducts
from models import *

from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

with app.app_context():
    db.drop_all() 
    db.create_all()

@app.route('/')
def home():
    return render_template("home.html")
  
@app.route('/home2')
def home2():
    return render_template("home2.html")  

@app.route('/receive',methods=['GET','POST'])
def receive():
    products = [(product.ProductID,product.ProductName) for product in Products.query.all()]
    form = ReceiveForm()
    form.Product.choices = products
    fields=[form.Product,form.LotNo,form.RecdDate,form.RecdInit,form.Certificate]
    buttons=[form.submit]

    if form.validate_on_submit():
        log_entry = Log(Product=form.Product.data,
        LotNumber=form.LotNo.data,
        DateReceived=form.RecdDate.data,
        ReceivedBy=form.RecdInit.data,
        Certificate=form.Certificate.data)
        db.session.add(log_entry)
        db.session.commit()

    return render_template("ReceiveForm.html", form=form, fields=fields, buttons=buttons)  

@app.route('/withdraw',methods=['GET','POST'])
def withdraw():
    form = WithdrawForm()
    fields=[form.Product,form.AvailableItem,form.WithdrawlDate,form.WithdrawlTech]
    buttons=[form.Withdraw,form.Certificate]
    return render_template("withdrawForm.html", form=form, fields=fields, buttons=buttons) 

@app.route('/AddProducts',methods=['GET','POST'])
def addProducts():
    form = AddProducts()
    fields=[form.ProductName,form.CatalogNumber,form.VendorID]
    buttons=[form.add]

    if form.validate_on_submit():
        product = Products(ProductName=form.ProductName.data,CatalogNumber=form.CatalogNumber.data,Vendor=form.VendorID.data)
        db.session.add(product)
        db.session.commit()

    return render_template("AddProducts.html",form=form,fields=fields,buttons=buttons)

@app.route('/AddVendors',methods=['GET','POST'])
def addVendors():
    form = AddVendors()
    fields=[form.VendorName]
    buttons=[form.add]

    if form.validate_on_submit():
        vendor = Vendors(VendorName=form.VendorName.data)
        db.session.add(vendor)
        db.session.commit()

    return render_template("AddVendors.html",form=form,fields=fields,buttons=buttons)

@app.route('/productList')
def productList():
    products = []
    results = db.session.query(Products).all()
    for result in results:
        products.append(result.ProductID)
    return render_template("productList.html", products=products)        

if __name__ == "__main__":
    app.run(debug=True)