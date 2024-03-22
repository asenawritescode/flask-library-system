from tests import TestFlaskApp

from app.models import *

class TestDatabaseEntries(TestFlaskApp):

    def test_create_read_update_book(self):
        """
        Test that a book can be created, read, and updated.
        """
        
        # Create a new book
        book = Book.create(name="This is a book", author="demo author", publication_date="2022-01-01", isbn="123456789", quantity=10, description="description")
        self.assertIsNotNone(book.id)

        # Read the created book
        read_book = Book.get(book.id)
        self.assertEqual(read_book.name, "This is a book")

        # Update the book
        book.update(name="This is an updated book")
        self.assertEqual(book.name, "This is an updated book")


    def test_create_read_update_user(self):
        """
        Test that a user can be created, read, and updated.
        """

        # Create a new user
        user = User.create(first_name="first_name", last_name="last_name", email="email@gmail.com", reg_number="reg_number", phone_number="+254758334490")
        self.assertIsNotNone(user.id)

        # Read the created user
        read_user = User.get(user.id)
        self.assertEqual(read_user.first_name, "first_name")

        # Update the user
        user.update(first_name="demo_updated")
        self.assertEqual(user.first_name, "demo_updated")

    def test_create_read_transaction(self):
        """
        Test that a transaction can be created and read
        """

        # Create a new transaction
        transaction=Transaction.create(user_id=1, book_id=1, quantity=1, units=1 , direction=1, fees=0)        
        self.assertIsNotNone(transaction.id)

        # Read the created transaction
        read_transaction = Transaction.get(transaction.id)
        self.assertEqual(read_transaction.quantity, 1)