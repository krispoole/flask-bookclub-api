from api.models.club import Club
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_club(obj, info, club_id):
    try:
        club = Club.query.get(club_id)
        payload = {
            "success": True,
            "club": club.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Club item matching id {club_id} does not exist."]
        }
    return payload

def resolve_clubs(obj, info):
    try:
        clubs = [club.to_dict() for club in Club.query.all()]
        payload = {
            "success": True,
            "clubs": clubs
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload