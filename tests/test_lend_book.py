from test import TestFlaskApp

from app.services.transactions.views import LendBook

class TestLendBook(TestFlaskApp):
    def test_lend_book(self):
        """
        Test that a book can be lent to a user
        """
        
        # Create a new book
        book = self.create_book()

        # Create a new user
        user = self.create_user()

        # Lend the book
        LendBook(user_id=user.reg_number, book_name=book.isbn, book_id=book.id)
