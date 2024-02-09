from flask import render_template, Blueprint, request
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
    
    if request.method == "POST":
        #todo:Grab data from form and Push user to database... 
        book_name = request.form.get('book_name')
        author = request.form.get('author')
        publication_date = request.form.get('publication_date')
        isbn = request.form.get('isbn')
        units = request.form.get('units')
        description = request.form.get('description')
        
        # Push book to database
        # book = Book(book_name=book_name, author=author, publication_date=publication_date, isbn=isbn, units=units, description=description)
        # db.session.add(book)
        # db.session.commit()

        # how can I do this above ?
        

        return {"message": "User created successfully!"}
    return render_template('books/create_book.html', active = 'actions')

# Add other routes here
# View, Delete, Add, Update Book data.