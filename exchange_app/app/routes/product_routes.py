from flask import Blueprint, jsonify, request, redirect, url_for
from ..repositories.product_repository import ProductRepository

product_bp = Blueprint('products', __name__)


@product_bp.route('/', methods=['GET'])
def list_products():
    products = ProductRepository.get_all_products()
    return jsonify(products)


@product_bp.route('/', methods=['POST'])
def create_product():
    name = request.form['name']
    price_usd = request.form['price_usd']
    source = request.form['source']
    price_pln = price_usd * 4
    ProductRepository.create_product(name, price_usd, price_pln, source)
    return redirect(url_for('home'))
    # sprawdź cenę po przekonwertowaniu# 4 zł
    # create_product(... te dane )
    # return 201 i added successfuly

