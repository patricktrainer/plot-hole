from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "a4f2d0f8ca8ffdf793fe0b9a0562f32e"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "users.login"

from plot_hole.main.routes import main
from plot_hole.posts.routes import posts
from plot_hole.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)
