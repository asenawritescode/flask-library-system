from flask import render_template, Blueprint, request

from app.models import Transaction, Book
from app.utils.decorators import *

transactions_bp = Blueprint(
    'transactions',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@check_book_availability
@check_user_permisson
def lendBook(user_id, book_id, units=1, direction=1, fees=0):
    demo=Transaction.create(user_id=user_id , book_id=book_id, units=units , direction=direction, fees=fees)
    book = Book.query.get(book_id)
    book.update(quantity = book.quantity - 1)
    print(demo)

@transactions_bp.route('/transactions', methods=['GET'])
def index():
    return render_template('transactions/index.html', active='transactions')

@transactions_bp.route('/transactions/create', methods=['POST'])
def create_transaction():
    
    book_name = request.form.get('book_value')
    user_name = request.form.get('user_value')

    try:
        # expect a class <class 'app.models.Transaction'>
        lendBook(user_name, book_name)

    except(Exception) as e:
        # print the exception and pass the feedback to flash message
        print(e)  
    
    # add a hook here to update the book quantity
    # check to consider (has borrowed book ?, is the book available for borrowing ?)

    return render_template('transactions/index.html', active='transactions')

 