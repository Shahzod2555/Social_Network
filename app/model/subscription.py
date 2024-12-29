from datetime import datetime

from ..extentions import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    subscribers_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    date_create = db.Column(db.DateTime, default=datetime.now)
