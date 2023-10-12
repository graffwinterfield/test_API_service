from app_main import db


class Questions(db.Model):
    __tablename__ = 'Questions'
    ID = db.Column(db.Integer, primary_key=True)
    ID_question = db.Column(db.Integer)
    Answer = db.Column(db.String(1000), nullable=False)
    Question = db.Column(db.String(1000), nullable=False)
    Created_at = db.Column(db.DateTime)
