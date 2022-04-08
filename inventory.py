from ast import Add
from flask import Flask, render_template
from forms import ReceiveForm, WithdrawForm

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home2')
def home2():
    return render_template("home2.html")  

@app.route('/receive')
def receive():
    form = ReceiveForm()
    return render_template("ReceiveForm.html", form=form)  

@app.route('/withdraw')
def withdraw():
    form = WithdrawForm()
    return render_template("withdrawForm.html", form=form) 

@app.route('/formtemplatetest')
def formtemplatetest():
    form = ReceiveForm()
    fields=[form.Product,form.LotNo,form.RecdDate,form.RecdInit]
    buttons=[form.submit]
    return render_template("ReceiveFormFromTemplate.html",form=form, fields=fields, buttons=buttons)

if __name__ == "__main__":
    app.run(debug=True)