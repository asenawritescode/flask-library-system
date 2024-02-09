from flask import render_template, Blueprint
reports_bp = Blueprint(
    'reports',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@reports_bp.route('/reports', methods=['GET', 'POST'])
def index():
    return render_template('reports/index.html', active='reports')