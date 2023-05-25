from main import db


class Review(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    rating = db.Column(db.Integer)
    date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "rating": self.rating,
            "date": str(self.date.strftime('%d-%m-%Y'))
        }