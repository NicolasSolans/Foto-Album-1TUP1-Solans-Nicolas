from . import db

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = True)
    image = db.Column(db.String, nullable = False)

    def __repr__(self) -> str:
        return f"<Foto {self.title}>"