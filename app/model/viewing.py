from datetime import datetime

from ..extentions import db


class Viewing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    publication = db.Column(db.Integer, db.ForeignKey('publication.id', ondelete='CASCADE'))

    created_at = db.Column(db.DateTime, default=datetime.now)
