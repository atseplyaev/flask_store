import os
from flask import Flask
from flask_migrate import Migrate
from store.models import db, Product
from store.views import bp
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def create_app(config_object_path = 'store.config.DevelopConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object_path)
    app.register_blueprint(bp)

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    admin = Admin(app, name='store', template_mode='bootstrap3')
    admin.add_view(ModelView(Product, db.session))

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass


    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
