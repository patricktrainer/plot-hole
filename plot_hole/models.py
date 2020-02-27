from datetime import datetime
from plot_hole import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.objects.get(id=id)


class User(UserMixin, db.Document):
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(max_length=50, required=True)
    password = db.StringField(required=True)


class Plot(db.Document):
    plot = db.PointField()
    plot_date = db.DateTimeField()
    author = db.ReferenceField(User)
