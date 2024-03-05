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
        if not count == 0 or count%2 == 0:
            raise(Exception("User has a pending book !"))        
        return func(user_name, book_name)
    return wrapper
