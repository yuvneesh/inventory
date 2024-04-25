import flask
from flask import Flask, jsonify, render_template, flash, redirect, url_for
import sqlite3
import pandas as pd

from db_tools import Dataman
from forms import AddVendors, ReceiveForm, WithdrawForm, AddProducts, DisposeForm

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

# Instantiating Dataman
dataman = Dataman("site.db")

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/receive',methods=['GET','POST'])
def receive():

    # Create the form
    form = ReceiveForm()
    fields=[form.ProductName,form.LotNumber,form.ReceivedBy,form.DateReceived,form.Certificate]
    buttons=[form.submit]
    products = dataman.get_products()
    form.ProductName.choices = products
    
    if flask.request.method == "POST":
        if form.validate_on_submit():
            item_number = dataman.receive_product(form.data)
            flash(f"Success! {form.ProductName.data} have been added. The item number for the new item is: {item_number}", 'success')
            return redirect(url_for("receive"))

    return render_template("ReceiveProduct.html", form=form, fields=fields, buttons=buttons)

@app.route('/get-item-numbers/<product>',methods=['GET'])
def get_item_numbers(product):
    serial_numbers = dataman.get_items_of_product(product)
    return jsonify({"SerialNumber": serial_numbers})

@app.route('/withdraw',methods=['GET','POST'])
def withdraw():
    form = WithdrawForm()
    fields=[form.ProductName,form.SerialNumber,form.DateWithdrawn,form.WithdrawnBy]
    buttons=[form.Withdraw,form.Certificate]
    form.ProductName.choices = dataman.get_products()
    form.SerialNumber.choices = []

    if flask.request.method == "POST":
        if form.validate_on_submit():
            if dataman.withdraw_product(form.data):
                flash(f"Succesfully withdrawn {form.data['ProductName']}-{form.data['SerialNumber']}", 'success')
                return redirect(url_for("withdraw"))
            else:
                flash(f"Failed to withdraw {form.data['ProductName']}-{form.data['SerialNumber']}", 'failure')

        
    return render_template("WithdrawProduct.html", form=form, fields=fields, buttons=buttons)

@app.route('/dispose',methods=['GET','POST'])
def dispose():
    form = DisposeForm()
    fields=[form.ProductName,form.SerialNumber,form.DateDisposed,form.DisposedBy]
    buttons=[form.Dispose]
    form.ProductName.choices = dataman.get_products()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            if dataman.withdraw_product(form.data):
                flash(f"Succesfully withdrawn {form.data['ProductName']}-{form.data['SerialNumber']}", 'success')
                return redirect(url_for("withdraw"))
            else:
                flash(f"Failed to withdraw {form.data['ProductName']}-{form.data['SerialNumber']}", 'failure')

        
    return render_template("DisposeProduct.html", form=form, fields=fields, buttons=buttons)

@app.route('/AddProducts',methods=['GET','POST'])
def addProducts():
    form = AddProducts()
    fields=[form.ProductName,form.CatalogNumber,form.VendorID]
    buttons=[form.add]

    if form.validate_on_submit():        
        dataman.add_product(form.data)

    return render_template("formTemplate.html",form=form,fields=fields,buttons=buttons)

@app.route('/AddVendors',methods=['GET','POST'])
def addVendors():
    form = AddVendors()
    fields=[form.VendorName]
    buttons=[form.add]

    if form.validate_on_submit():
        return "Method not implemented"

    return render_template("formTemplate.html",form=form,fields=fields,buttons=buttons)


if __name__ == "__main__":

    app.run(debug=True, port=5001)

    