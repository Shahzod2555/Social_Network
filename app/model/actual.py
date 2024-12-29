from ..extentions import db
from datetime import datetime


class Actual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    description = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    mentions = db.Column(db.String(255), nullable=True)
    is_activ = db.Column(db.Boolean, default=False)

    image = db.Column(db.String(255))

    actual_image = db.relationship('ActualImage', backref='actual', cascade="all, delete-orphan")
    actual_video = db.relationship('ActualVideo', backref='actual', cascade="all, delete-orphan")
    actual_audio = db.relationship('ActualAudio', backref='actual', cascade="all, delete-orphan")

    create_date = db.Column(db.DateTime, default=datetime.now)


class ActualImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    actual_id = db.Column(db.Integer, db.ForeignKey('actual.id', ondelete='CASCADE'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))


class ActualVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(255))
    actual_id = db.Column(db.Integer, db.ForeignKey('actual.id', ondelete='CASCADE'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))


class ActualAudio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audio = db.Column(db.String(255))
    actual_id = db.Column(db.Integer, db.ForeignKey('actual.id', ondelete='CASCADE'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
