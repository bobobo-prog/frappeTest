from flask import Flask,render_template,flash,redirect
from flask.helpers import url_for
from frappe_test.models import Product,ProductMovement
from frappe_test import app
from frappe_test.forms import AddProductForm,AddLocationForm

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/addproduct",methods= ['GET','POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'{form.prod_name.data} Added to Inventory!','success')
        return redirect(url_for('add_product'))

    return render_template('addproduct.html',title = 'Add Product',form = form)

@app.route("/addlocation",methods = ['GET','POST'])
def add_location():
    form = AddLocationForm()
    if form.validate_on_submit():
        flash(f'{form.loc_id.data} Added to Inventory!','success')
        return redirect(url_for('add_location'))

    return render_template('addlocation.html',title = 'Add Location',form = form)
