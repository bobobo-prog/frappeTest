from flask_sqlalchemy import SQLAlchemy
from frappe_test import db
from datetime import datetime


class Product(db.Model):
    product_id  = db.Column(db.Text,primary_key =True)
    product_name = db.Column(db.String(20),nullable = False,unique = True)
    relation = db.relationship('ProductMovement',lazy = True)
    def __repr__(self):
        return f"Product('{self.product_id}','{self.product_name}')"


class Location(db.Model):
    location_id  = db.Column(db.Text,primary_key =True)
    address = db.Column(db.String(20),nullable = False,unique = True)

    def __repr__(self):
        return f"Product('{self.location_id}','{self.address}')"


class ProductMovement(db.Model):
    movement_id = db.Column(db.Text,primary_key = True,unique = True)
    timestamp = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    from_location = db.Column(db.Text)
    to_location = db.Column(db.Text)
    product_id = db.Column(db.Text,db.ForeignKey('product.product_id'),nullable= False)
    quantity = db.Column(db.Integer)
    

    def __repr__(self):
        return f"Product('{self.movement_id}','{self.timestamp}','{self.from_location}','{self.to_location}','{self.product_id}','{self.quantity}')"


