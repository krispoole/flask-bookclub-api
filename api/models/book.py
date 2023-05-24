from main import db


class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year_of_publication = db.Column(db.Integer)
    genre = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year_of_publication": self.year_of_publication,
            "genre": self.genre,
        }