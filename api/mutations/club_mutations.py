from ariadne import convert_kwargs_to_snake_case

from main import db
from api.models.club import Club


@convert_kwargs_to_snake_case
def resolve_create_club(obj, info, name, description):
    try:
        club = Club(
            name=name,
            description= description
        )
        db.session.add(club)
        db.session.commit()
        payload = {
            "success": True,
            "club": club.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect format"]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_club(obj, info, club_id):
    try:
        club = Club.query.get(club_id)
        db.session.delete(club)
        db.session.commit()
        payload = {"success": True}
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Club matching id {club_id} not found"]
        }
    return payload