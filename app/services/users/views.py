from flask import render_template, Blueprint
users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@users_bp.route('/users', methods=['GET', 'POST'])
def index():
    return render_template('users/index.html', active='users')