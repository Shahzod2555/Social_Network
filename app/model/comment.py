from datetime import datetime

from ..extentions import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    publication = db.Column(db.Integer, db.ForeignKey('publication.id', ondelete='CASCADE'))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
