from ariadne import convert_kwargs_to_snake_case

from main import db
from api.models.user import User
from api.models.club import Club


@convert_kwargs_to_snake_case
def resolve_create_user(obj, info, email, password):
    try:
        user = User(
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect email format"]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_user(obj, info, user_id):
    try:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        payload = {"success": True}
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User matching id {user_id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_add_club_to_user(obj, info, user_id, club_id):
    try:
        user = User.query.get(user_id)
        club = Club.query.get(club_id)
        if not user or not club:
            payload = {
                "success": False,
                "errors": [f"User or Club not found"]
            }
        else:
            user.clubs.append(club)
            db.session.commit()
            payload = {
                "success": True,
                "user": user.to_dict()
            }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload