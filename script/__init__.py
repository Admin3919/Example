from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from exts.auth import Auth


# 包含了SQLAlchemy相关的所有操作
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from .views.acccount import ac
    from .views.home import hm
    app.register_blueprint(ac)
    app.register_blueprint(hm)

    db.init_app(app)

    Auth(app)

    return app