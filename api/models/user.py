from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "password": self.password
        }