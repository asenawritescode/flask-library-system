from flask import render_template, Blueprint
transactions_bp = Blueprint(
    'transactions',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@transactions_bp.route('/transactions', methods=['GET', 'POST'])
def index():
    return render_template('transactions/index.html', active='transactions')