from flask import render_template, Blueprint, request
users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@users_bp.route('/users', methods=['GET', 'POST'])
def index():
    return render_template('users/index.html', active='users')

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
        # user = User(first_name=first_name, last_name=last_name, email=email)
        # db.session.add(user)
        # db.session.commit()

        return {"message": "User created successfully!"}
    return render_template('users/create_user.html', active ='actions')