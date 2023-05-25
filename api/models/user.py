from main import db
from api.association_tables.user_club import user_club_association


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    clubs = db.relationship(
        "Club", secondary=user_club_association, back_populates="users"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "clubs": [club.to_dict() for club in self.clubs]
        }
    
    def to_dict_without_clubs(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }