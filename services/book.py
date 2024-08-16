from models.book import Book as BookModel
from schemas.book import Book

class BookServices():
    def __init__(self, db) -> None:
        self.db = db

    def get_books(self):
        result =

    def get_book(self, book_id):

    def create_book(self, book : Book):

    def update_book(self, book_id : int, data : Book):

    def delete_book(self, book_id : int):