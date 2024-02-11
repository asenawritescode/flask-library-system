from flask import render_template, Blueprint, request

from app import db
from app.models import User

users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@users_bp.route('/users', methods=['GET', 'POST'])
def index():

    users = User.get_all()

    return render_template('users/index.html', active='users', users=users)

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
        except:
            # this message shouled be flashed to the user
            # flash
            return {"message": "User not created!"}
        
        return render_template('users/index.html', active ='dashboard')
    return render_template('users/create_user.html', active ='actions')