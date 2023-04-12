# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime
# from sqlalchemy import Column, String, Integer

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    poster = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, desc, poster):
        self.title = title
        self.desc = desc
        self.poster = poster

    def __repr__(self):
        return '<Movies %r>' % (self.title)

# class Movies(db.model):
#     __tablename__ = 'movies'

#     # id = db.column(db.Integer, primary_key=True)
#     # title = db.column(db.String)
#     # desc = db.column(db.String)
#     # poster = db.column(db.String)
#     # created_at = db.column(db.DateTime, default=datetime.datetime.utcnow)
#     id = Column(Integer, primary_key=True)
#     title = Column(String(80))
#     desc = Column(String)
#     poster = Column(String)
#     created_at = Column(db.DateTime, default=datetime.utcnow)

#     def __init__(self, title, desc, poster):
#         self.title = title
#         self.desc = desc
#         self.poster = poster

#     # def __repr__(self):
#     #     return '<Movies %r>' % (self.title)