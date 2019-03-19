"""Serealizer."""

from flask_marshmallow import Marshmallow
from .model import Product

ma = Marshmallow()


def configure(app):
    """Init serializer."""
    ma.init_app(app)


class ProductSchema(ma.Schema):
    """Product Shcema."""
    class Meta():
        """Product Shcema."""
        fields = ('id', 'description', 'price', 'qty')


product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)
