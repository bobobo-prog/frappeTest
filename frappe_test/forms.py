
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.fields.core import IntegerField, TimeField 
from wtforms.validators import DataRequired, data_required,Length

class AddProductForm(FlaskForm):
    prod_id = StringField('Product ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    prod_name = StringField('Product Name',validators=[DataRequired(),Length(max = 20)])
    submit = SubmitField('Add Product') 

class AddLocationForm(FlaskForm):
    loc_id = StringField('Location ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    loc_name = StringField('Address',validators=[DataRequired(),Length(max = 20)])
    submit = SubmitField('Add Location') 

class AddProdMovement(FlaskForm):
    movement_id = StringField('Movement ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    from_location = StringField('From Location',validators=[DataRequired()])
    to_location = StringField('To Location',validators=[DataRequired()])
    product_id = StringField('Product ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    quantity = IntegerField('Quantity',validators=[DataRequired()])
    submit = SubmitField('Add Movement')
