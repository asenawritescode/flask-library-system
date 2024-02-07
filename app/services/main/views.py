from flask import render_template, Blueprint
main_bp = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@main_bp.route('/')
def index():
    return render_template('shared/_dashboard.html', active='dashboard')