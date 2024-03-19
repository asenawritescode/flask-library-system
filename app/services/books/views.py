from math import ceil
from flask import render_template, Blueprint, request, redirect, url_for

from app.models import Book
from app.utils.convert_date import convert
from configs import *

book_bp = Blueprint(
    'book',
    __name__,
    template_folder='templates',
    url_prefix='/'
)


@book_bp.route('/books', methods=['GET', 'POST'])
def index():

    page = request.args.get('page', 1, type=int)

    paginated_data = Book.paginate(page=page, per_page=RESULTS_PER_PAGE)

    return render_template('books/index.html', active = 'books', books=paginated_data.items or 'Hakuna', pagination=paginated_data)


@book_bp.route('/books/create', methods=['GET', 'POST'])
def create_book():
    
    if request.method == "POST":
        #todo:Grab data from form and Push user to database... 
        book_name = request.form.get('book_name')
        author = request.form.get('author')
        publication_date = convert(request.form.get('publication_date'))
        isbn = request.form.get('isbn')
        units = request.form.get('units')
        description = request.form.get('description')

        # Push book to database
        try:
            Book.create(name=book_name, author=author, publication_date=publication_date, isbn=isbn, quantity=units, description=description)
            return redirect(url_for('.index'))
        except:
        #     # this message shouled be flashed to the user
        #     # flash
            return {"message": "Book not created!"}
        
    return render_template('books/create_book.html', active = 'actions')