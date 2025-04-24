from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.middleware.middleware import Middleware

app = Flask(__name__, template_folder='view')

app.config['SECRET_KEY'] = "Xn2r5u8x/A?D(G+KbPeShVmYq3s6v9y$B&E)H@McQfTjWnZr4u7w!z%C*F-JaNdR"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dika.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
# Middleware 
app.wsgi_app = Middleware(app.wsgi_app)

from app.model import worker, role, shift, permission
from app.controller import worker, shift
