from datetime import datetime
from plot_hole import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.objects(id=id).first()


class User(UserMixin, db.Document):
    email = db.EmailField(unique=True)
    username = db.StringField(max_length=50)
    password = db.StringField()
    meta = {"allow_inheritance": True}


class Plot(db.Document):
    plot = db.PointField()
    plot_date = db.DateTimeField(default=datetime.utcnow)
    user = db.ReferenceField(User)
