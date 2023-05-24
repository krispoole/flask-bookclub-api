from api.models.user import User
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_user(obj, info, user_id):
    try:
        user = User.query.get(user_id)
        payload = {
            "success": True,
            "user": user.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User item matching id {user_id} not found"]
        }
    return payload

def resolve_users(obj, info):
    try:
        users = [user.to_dict() for user in User.query.all()]
        payload = {
            "success": True,
            "users": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload