from main import db


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }