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

@bp.route('/products/<int:product_id>', endpoint='product')
def products_page(product_id):
    product = Product.query.first_or_404(product_id)
    return render_template('product.html', product=product)
