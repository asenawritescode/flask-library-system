from sqlalchemy import func
from app import db

def get_book_user_dict(Transaction, User, Book):
    
    # fetch all users in the database
    users = User.get_all_from('id','first_name','last_name','reg_number')
    
    # format with the structure {id : f"{first_name} {last_name} - {reg_number}"}
    user_result = {}
    for user in users:
        user_result[user.id] = f"{user.first_name} {user.last_name} - {user.reg_number}"

    # fetch all books in the database
    books = Book.get_all_from('id','isbn', 'name')

    # format with the structure {id : f"{isbn} - {name}"}
    book_result = {}
    for book in books:
        book_result[book.id] = f"{book.isbn} - {book.name}"
        
    # Retrieve user IDs with odd transaction counts and their latest transactions
    odd_user_transactions = db.session.query(
        Transaction.user_id,
        func.max(Transaction.created_at).label('latest_transaction')
    ).group_by(Transaction.user_id).having(func.count() % 2 != 0).all()

    # Create a dictionary to store book IDs and corresponding user IDs
    book_user_dict = {}

    # Iterate through the odd_user_transactions
    for user_id, latest_transaction in odd_user_transactions:
        
        # Retrieve the book ID for the latest transaction of the user
        latest_book_transaction = Transaction.query.filter_by(user_id=user_id, created_at=latest_transaction).first()
        book_id = latest_book_transaction.book_id
        book_diplay = book_result[book_id]
        
        # Add the user ID and display name to the list of user IDs for the corresponding book ID
        book_user_dict.setdefault(book_id, {'name': book_diplay, 'users': []})['users'].append({'id': user_id, 'display': user_result[user_id]})

    return book_user_dict       