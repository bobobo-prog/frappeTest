from datetime import datetime
from enum import unique
from flask import Flask,render_template,flash,redirect
from flask.helpers import url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1be7ae4e90628356923896e8cb6b1159'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from frappe_test import routes

