from flask import render_template, Blueprint, jsonify
from app.models import Book, User
main_bp = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

# def row2dict(row_data):
#     result = {}
#     for row in row_data:
#         result.append({
#             'id': row.id,
#             'isbn': row.isbn,
#         })
#     return result

@main_bp.route('/')
def index():
    return render_template('shared/_dashboard.html', active='dashboard')

@main_bp.route('/get-data', methods=['POST', 'GET'])
def get_data():
    # get users from database
    users = User.get_all_from('id','first_name','last_name','reg_number')
    
    user_result = []
    for user in users:
        user_result.append({
            # 'id': user.id,
            'name': user.first_name + '' + user.last_name +' - '+ user.reg_number,
            # 'reg_number': user.reg_number
        })

    # get books whose availability is more than 1 from database
    available_books = Book.get_all_from('id','isbn' )

    book_result = []
    for book in available_books:
        book_result.append({
            # 'id': book.id,
            'isbn': book.isbn
        })

    # return json object with available_books and users
    return jsonify({'users': user_result, 'books': book_result})
