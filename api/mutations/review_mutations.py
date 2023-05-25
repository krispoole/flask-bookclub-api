from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from main import db
from api.models.review import Review


@convert_kwargs_to_snake_case
def resolve_create_review(obj, info, title, body, rating, date):
    try:
        date = datetime.strptime(date, '%d-%m-%Y').date()
        review = Review(
            title=title,
            body=body,
            rating=rating,
            date=date
        )
        db.session.add(review)
        db.session.commit()
        payload = {
            "success": True,
            "review": review.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format"]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_review(obj, info, review_id):
    try:
        review = Review.query.get(review_id)
        db.session.delete(review)
        db.session.commit()
        payload = {"success": True}
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Review matching id {review_id} not found"]
        }
    return payload