import os
from flask import Flask
from flask_migrate import Migrate
from store.models import db

from store.views import bp

def create_app(config_object_path = 'store.config.DevelopConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object_path)
    app.register_blueprint(bp)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        return "<h1>Hello World!</h1>"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
