from flask import render_template, Blueprint, request, redirect, url_for

from app.models import Transaction, Book, User
from app.utils.decorators import *
from configs import *

transactions_bp = Blueprint(
    'transactions',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

@check_book_availability
@check_user_permisson
def lendBook(user_id, book_id, book_name, units=1, direction=1, fees=0):
    demo=Transaction.create(user_id=user_id, book_id=book_id, units=units , direction=direction, fees=fees)
    book = Book.get(book_name)
    book.update(quantity = book.quantity - 1)
    print(demo)

@check_book_lend
def returnBook(user_id, book_id, book_name, units=1, direction=0, fees=0):
    return_book = Transaction.create(user_id=user_id , book_id=book_name, units=units , direction=direction, fees=fees)
    book = Book.filter_by(isbn=book_id).first()
    book.update(quantity = book.quantity + 1)
    print(return_book)

@transactions_bp.route('/transactions', methods=['GET'])
def index():
    # Get the transactions
    page = request.args.get('page', 1, type=int)

    paginated_data = Transaction.paginate(page=page, per_page=RESULTS_PER_PAGE)



    return render_template('transactions/index.html', active='transactions', transactions=paginated_data.items or 'Hakuna', pagination=paginated_data or 'Hakuna')

@transactions_bp.route('/transactions/create', methods=['POST'])
def create_transaction():
    # Get the resource arg
    url_data = request.args.get('resource')

    if url_data == "lendbook":
            
        book_name = request.form.get('book_value')
        user_name = request.form.get('user_value')

        try:
            # expect a class <class 'app.models.Transaction'>
            
            # get data from books and users
            book_lent = Book.get(book_name)
            user_lent = User.get(user_name)

            lendBook(user_id=user_lent.reg_number, book_id=book_name, book_name=book_lent.isbn)
            return redirect(url_for('.index'))
        except(Exception) as e:
            # print the exception and pass the feedback to flash message
            print(e)
            # flash
            return {"message": "Transaction not created!"} 
        
        # add a hook here to update the book quantity
        # check to consider (has borrowed book ?, is the book available for borrowing ?)
    elif url_data == "receivebook":

        book_name = request.form.get('book_value')
        user_name = request.form.get('user_value')

        try:
            # expect a class <class 'app.models.Transaction'>
            book_lent = Book.filter_by(isbn=book_name).first()
            user_lent = User.filter_by(reg_number=user_name).first()

            # get the fees to be paid by the user

            returnBook(user_id=user_lent.reg_number, book_id=book_name, book_name=book_lent.isbn)
            return redirect(url_for('.index'))

        except(Exception) as e:
            # print the exception and pass the feedback to flash message
            # Get file that generated the exception
            print(e.__class__.__name__)
            print(type(e))
            print(e.args)
            print(e)
            # flash
            return {"message": "Transaction not created!"} 