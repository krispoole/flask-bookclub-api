from main import db
from api.association_tables.user_club import user_club_association

class Club(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    users = db.relationship(
        "User", secondary=user_club_association, back_populates="clubs"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "users": [user.to_dict_without_clubs() for user in self.users]
        }