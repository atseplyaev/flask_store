from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text)
    description = db.Column(db.String(255))
    name = db.Column(db.String(80), unique=True, nullable=False)
    display_size = db.Column(db.Float, nullable=False)
    cpu = db.Column(db.String(32), nullable=False)
    gpu = db.Column(db.String(32), nullable=False)
    ram_size = db.Column(db.Integer, nullable=False)
    rom_size = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.name
