from flask import Flask, render_template
from forms import AddVendors, ReceiveForm, WithdrawForm, AddProducts
from models import *

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

with app.app_context():
    #db.drop_all() 
    db.create_all()

@app.route('/')
def home():
    return render_template("home.html")
  
@app.route('/home2')
def home2():
    return render_template("home2.html")  

@app.route('/receive',methods=['GET','POST'])
def receive():
    form = ReceiveForm()
    fields=[form.Product,form.LotNo,form.RecdDate,form.RecdInit]
    buttons=[form.submit]
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
    fields=[form.Product,form.CatalogNumber,form.VendorID]
    buttons=[form.add]

    if form.validate_on_submit():
        product = Products(ProductID=form.Product.data,CatalogNumber=form.CatalogNumber.data,Vendor=form.VendorID.data)
        db.session.add(product)
        db.session.commit()

    return render_template("AddProducts.html",form=form,fields=fields,buttons=buttons)

@app.route('/AddVendors',methods=['GET','POST'])
def addVendors():
    form = AddVendors()
    fields=[form.VendorID,form.VendorName]
    buttons=[form.add]

    if form.validate_on_submit():
        vendor = Vendors(VendorID=form.VendorID.data, VendorName=form.VendorName.data)
        db.session.add(vendor)
        db.session.commit()

    return render_template("AddVendors.html",form=form,fields=fields,buttons=buttons)

        

if __name__ == "__main__":
    app.run(debug=True)