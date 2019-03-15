"""."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    """Init app.db."""
    db.init_app(app)
    app.db = db


class Product(db.Model):
    """Product DB."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        """Init DB product variable."""
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
