from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from henryjh.config import Config
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    from henryjh.users.routes import users
    from henryjh.posts.routes import posts
    from henryjh.main.routes import main
    from henryjh.category.routes import category
    # from henryjh.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(category)
    # app.register_blueprint(errors)

    return app