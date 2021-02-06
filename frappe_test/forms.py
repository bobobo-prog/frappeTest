
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, data_required,Length

class AddProductForm(FlaskForm):
    prod_id = StringField('Product ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    prod_name = StringField('Product Name',validators=[DataRequired(),Length(max = 20)])
    submit = SubmitField('Add Product') 

class AddLocationForm(FlaskForm):
    loc_id = StringField('Location ID',validators=[DataRequired(),Length(max = 4,min = 4)])
    loc_name = StringField('Address',validators=[DataRequired(),Length(max = 20)])
    submit = SubmitField('Add Location') 
