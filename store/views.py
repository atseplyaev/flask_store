from flask import Blueprint, render_template, current_app
from .models import Product
bp = Blueprint('index', __name__)


@bp.route('/', endpoint='index')
def index_page():
    products = Product.query.all()
    return render_template('index.html', products=products)


@bp.route('/products/', endpoint='products')
def products_page():
    products = Product.query.all()
    return render_template('products.html', products=products)

