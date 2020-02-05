from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
app.config["SECRET_KEY"] = "a4f2d0f8ca8ffdf793fe0b9a0562f32e"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["GOOGLEMAPS_KEY"] = "AIzaSyBPqujQqgSqi1gCUcXsrdmt7A0yvDVlzlw"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
GoogleMaps(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from plot_hole import routes
