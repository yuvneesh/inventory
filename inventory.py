from flask import Flask, render_template
from forms import ReceiveForm, WithdrawForm, AddMaterials
from models import *

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

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

@app.route('/AddMaterials',methods=['GET','POST'])
def addmaterials():
    form = AddMaterials()
    fields=[form.Product,form.CatalogNumber]
    buttons=[form.add]

    if form.validate_on_submit():
        Material = MaterialsList(Product=form.Product.data,CatalogNumber=form.CatalogNumber.data)
        db.session.add(Material)
        db.session.commit()
        print('Entry added to database')

    return render_template("AddMaterials.html",form=form,fields=fields,buttons=buttons)


        

if __name__ == "__main__":
    app.run(debug=True)