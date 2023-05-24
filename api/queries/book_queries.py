from api.models.book import Book
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_book(obj, info, book_id):
    try:
        book = Book.query.get(book_id)
        payload = {
            "success": True,
            "book": book.to_dict()
        } 
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Book item matching id {book_id} not found"]
        }
    return payload

def resolve_books(obj, info):
    try:
        books = [book.to_dict() for book in Book.query.all()]
        payload = {
            "success": True,
            "books": books
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload