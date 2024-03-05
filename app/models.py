from . import db
# from flask_sqlalchemy.event import listen_for
from datetime import datetime


class CRUDMixin:
    """Mixin that adds convenience methods for CRUD operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record."""
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def get(cls, id):
        """Get a record by its primary key."""
        return cls.query.get(id)

    def update(self, commit=True, **kwargs):
        """Update the attributes of the instance."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Delete the record from the database."""
        db.session.delete(self)
        if commit:
            db.session.commit()

    @classmethod
    def get_all(cls):
        """Get all records."""
        return cls.query.all()

    @classmethod
    def get_all_from(cls, *columns, **kwargs):
        """Get all records."""
        column_objects = [getattr(cls, column) for column in columns]
        return cls.query.filter_by(**kwargs).with_entities(*column_objects).all()

    @classmethod
    def filter_by(cls, **kwargs):
        """Filter records by given criteria."""
        return cls.query.filter_by(**kwargs)

    @classmethod
    def paginate(cls, page, per_page, **kwargs):
        """Paginate records."""
        return cls.query.paginate(page=page, per_page=per_page, error_out = False)    
        
    @classmethod
    def search(cls, query, page=1, per_page=10):
        """Search records based on query."""
        return cls.query.filter(cls.__searchable__.match(query)).paginate(page, per_page, False)
        

class Book(db.Model, CRUDMixin):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(37), nullable=False)
    author = db.Column(db.String(37), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

class User(db.Model, CRUDMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(37), nullable=False)
    last_name = db.Column(db.String(37), nullable=False)
    reg_number = db.Column(db.Integer, nullable=False, unique=True)
    phone_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(37), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

class Transaction(db.Model, CRUDMixin):

    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.Integer, nullable=False)
    fees = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    user = db.relationship('User', backref='transactions')
    book = db.relationship('Book', backref='transactions')


