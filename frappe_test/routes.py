from flask import Flask,render_template,flash,redirect
from flask.helpers import url_for
from frappe_test.models import Location, Product,ProductMovement
from frappe_test import app
from frappe_test.forms import AddProdMovement, AddProductForm,AddLocationForm
from frappe_test import db

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/addproduct",methods= ['GET','POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product = Product(product_id = form.prod_id.data,product_name = form.prod_name.data)
        db.session.add(product)
        db.session.commit()
        flash(f'{form.prod_name.data} Added to Inventory!','success')
        return redirect(url_for('add_product'))

    data = Product().query.filter_by().all()
    return render_template('addproduct.html',title = 'Add Product',form = form,data = data)

@app.route("/addlocation",methods = ['GET','POST'])
def add_location():
    form = AddLocationForm()
    if form.validate_on_submit():
        location = Location(location_id = form.loc_id.data,address = form.loc_name.data)
        db.session.add(location)
        db.session.commit()
        flash(f'{form.loc_id.data} Added to Database!','success')
        return redirect(url_for('add_location'))

    data = Location().query.filter_by().all()
    return render_template('addlocation.html',title = 'Add Location',form = form,data = data)


@app.route("/addproductmovement",methods = ['GET','POST'])
def add_prodmovement():
    form = AddProdMovement()
    if form.validate_on_submit():
        movement = ProductMovement(movement_id = form.movement_id.data,from_location = form.from_location.data,to_location = form.to_location.data,product_id = form.product_id.data,quantity = form.quantity.data)
        db.session.add(movement)
        db.session.commit()
        flash(f'{form.movement_id.data} Added to Database!','success')
        return redirect(url_for('add_prodmovement'))
    data = ProductMovement().query.filter_by().all()
    return render_template('addproductmovement.html',title = 'Add Movement Data',form = form,data = data)
    
