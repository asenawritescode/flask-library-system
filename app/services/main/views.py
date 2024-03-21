from flask import render_template, Blueprint, jsonify, request
from app.models import Book, User, Transaction

from app.utils.get_user_book import get_book_user_dict

main_bp = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    url_prefix='/'
)



@main_bp.route('/')
def index():
    return render_template('shared/_dashboard.html', active='dashboard')

@main_bp.route('/get-data', methods=['POST', 'GET'])
def get_data():
    # get data passed in url 
    url_data = request.args.get('resource')
    if url_data == "lendbook":
        # get users from database
        users = User.get_all_from('id','first_name','last_name','reg_number')
        
        user_result = []
        for user in users:
            user_result.append({
                'id': user.id,
                'name': user.first_name + '' + user.last_name ,
                'reg_number': user.reg_number,
                'display': f"{user.first_name} {user.last_name} - {user.reg_number}"
            })
            # user_result.append(f"{user.first_name} {user.last_name} - {user.reg_number}")

        # get books whose availability is more than 1 from database
        available_books = Book.get_all_from('id','isbn', 'name',  )

        book_result = []
        for book in available_books:
            book_result.append({
                'id': book.id,
                'isbn': book.isbn,
                'display': f"{book.isbn} - {book.name}"
            })
            # conert int to str
            
            # book_result.append(f"{book.isbn} - {book.name}")

        # return json object with available_books and users
        return jsonify([book_result, user_result])

    elif url_data == "receivebook":
        data = get_book_user_dict(Transaction, User, Book)
        return  jsonify(data)
        