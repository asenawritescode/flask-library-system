import unittest
from app import create_app, db  # Import your Flask application and database instance
from app.models import *

class TestFlaskApp(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the Flask app for testing.
        """
        
        app = create_app('testing')  # Create a Flask app instance
        app.config['TESTING'] = True  # Set TESTING config to True
        return app

    def setUp(self):
        """
        Set up any resources needed for testing.
        """
        
        db.create_all()  # Create database tables before each test

    def tearDown(self):
        """
        Clean up after each test.
        """

        db.session.remove()  # Close database session after each test
        db.drop_all()  # Drop all database tables after each test

    def create_user():
        """
        Create a new user.
        """
        user = User.create(first_name="first_name", last_name="last_name", email="email@gmail.com", reg_number="LIB-001", phone_number="+254758334490")

        return user

    def create_book():
        """
        Create a new book.
        """
        book = Book.create(name="This is a book", author="demo author", publication_date="2022-01-01", isbn="123456789", quantity=10, description="description")

        return book
    

if __name__ == '__main__':
    unittest.main()