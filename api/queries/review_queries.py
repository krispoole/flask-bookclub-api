from api.models.review import Review
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_review(obj, info, review_id):
    try:
        review = Review.query.get(review_id)
        payload = {
            "success": True,
            "review": review.to_dict()
        } 
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Review item matching id {review_id} not found"]
        }
    return payload

def resolve_reviews(obj, info):
    try:
        reviews = [review.to_dict() for review in Review.query.all()]
        payload = {
            "success": True,
            "reviews": reviews
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload