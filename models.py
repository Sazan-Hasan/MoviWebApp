from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    movies = db.relationship("Movie", backref="user", lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    director = db.Column(db.String)
    year = db.Column(db.Integer)
    poster_url = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"Movie(id={self.id}, name='{self.name}', user_id={self.user_id})"