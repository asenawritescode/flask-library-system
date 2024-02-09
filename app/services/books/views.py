from flask import render_template, Blueprint
book_bp = Blueprint(
    'book',
    __name__,
    template_folder='templates',
    url_prefix='/'
)


@book_bp.route('/books', methods=['GET', 'POST'])
def index():

    return render_template('books/index.html', active = 'books')


@book_bp.route('/books/create', methods=['GET', 'POST'])
def create_book():
    
    return render_template('books/create_book.html', active = 'actions')

# Add other routes here
# View, Delete, Add, Update Book data.