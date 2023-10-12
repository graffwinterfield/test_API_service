from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, AdminIndexView

from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from models import Questions
    admin = Admin(app, index_view=AdminIndexView(url='/admin/'), template_mode='bootstrap4')
    admin.add_view(ModelView(Questions, db.session))
    return app
