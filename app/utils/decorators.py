from app.models import Transaction, Book
def check_book_availability(func):
    """
    Decorator to check book availability before calling the decorated function.
    """
    def wrapper(user_name, book_name):
        # Check if book quantity count is more than 1
        if Book.get(book_name) == None:
            raise(Exception("Book not found"))
        elif Book.get(book_name).quantity < 1:
            raise(Exception("Book not available"))
        return func(user_name, book_name)
    return wrapper

def check_user_permisson(func):
    def wrapper(user_name, book_name):
        # Check if book quantity count is more than 1           
        count = Transaction.filter_by(user_id = user_name).count()
        print("count" + str(count))
        if not count%2 == 0:
            raise(Exception("User has a pending book !"))        
        return func(user_name, book_name)
    return wrapper

def check_book_lend(func):
    def wrapper(user_id, book_id):
        # Check if user borrowed the book, find the most recent transaction by user then check if book id match
        recent_transaction = Transaction.filter_by(user_id = user_id).order_by(Transaction.created_at.desc()).first()

        # Check if book id match, raise error if not
        if not str(recent_transaction.book_id) == str(book_id):
            raise(Exception("User has not borrowed this book !"))
       
        return func(user_id, book_id)
    return wrapper

