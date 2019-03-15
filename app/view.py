"""Views ."""

from flask import Blueprint, jsonify, request
from .serealizer import ProductSchema
from .model import Product, db


bp_main = Blueprint('main', __name__)


product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)


@bp_main.route('/', methods=['GET'])
def home():
    """Home page."""
    return jsonify({ 'msg': 'Hello World' })


@bp_main.route('/product', methods=['POST'])
def add_product():
    """Add product."""
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


@bp_main.route('/product', methods=['GET'])
def get_products():
    """Get all Product."""
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result)


@bp_main.route('/product/<id>', methods=['GET'])
def get_product(id):
    """Get single Product."""
    product = Product.query.get(id)    

    return product_schema.jsonify(product)


@bp_main.route('/product/<id>', methods=['PUT'])
def update_product(id):
    """Get update Product."""

    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)


@bp_main.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    """Delete Product."""
    product = Product.query.get(id)    

    db.session.delete(product)

    db.session.commit()

    return product_schema.jsonify(product)
