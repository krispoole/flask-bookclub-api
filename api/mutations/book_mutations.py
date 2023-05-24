from ariadne import convert_kwargs_to_snake_case

from main import db
from api.models.book import Book


@convert_kwargs_to_snake_case
def resolve_create_book(obj, info, title, author, year_of_publication, genre):
    try:
        book = Book(
            title=title,
            author=author,
            year_of_publication=year_of_publication,
            genre=genre,
        )
        db.session.add(book)
        db.session.commit()
        payload = {
            "success": True,
            "book": book.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect format"]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_book(obj, info, book_id):
    try:
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        payload = {"success": True}
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User matching id {book_id} not found"]
        }
    return payload