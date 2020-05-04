from henryjh import db, login_manager
from datetime import datetime
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"
    


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.category_name}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.category_id}', '{self.date_posted}')"


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, server_default='default.jpg')

