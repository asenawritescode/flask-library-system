from flask import render_template, Blueprint, request, redirect, url_for

from app import db
from app.models import User
from configs import *

users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@users_bp.route('/users', methods=['GET', 'POST'])
def index():

    page = request.args.get('page', 1, type=int)

    paginated_data = User.paginate(page=page, per_page=RESULTS_PER_PAGE)

    return render_template('users/index.html', active='users', users=paginated_data.items, pagination = paginated_data)

@users_bp.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == "POST":
        #todo:Grab data from form and Push user to database... 
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        reg_number = request.form.get('reg_number')
        phone_number = request.form.get('phone_number')
        
        # Push user to database
        try:
            User.create(first_name=first_name, last_name=last_name, email=email, reg_number=reg_number, phone_number=phone_number)
            return redirect(url_for('.index'))
        except:
            # this message shouled be flashed to the user
            # flash
            return {"message": "User not created!"}
        
    return render_template('users/create_user.html', active ='actions')