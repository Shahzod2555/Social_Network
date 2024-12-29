from datetime import datetime

from .comment import Comment
from .viewing import Viewing
from .like import Like

from ..extentions import db


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

    images = db.relationship('PublicImage', backref='publication_images', cascade="all, delete-orphan")
    videos = db.relationship('PublicVideo', backref='publication_videos', cascade="all, delete-orphan")
    audios = db.relationship('PublicAudio', backref='publication_audios', cascade="all, delete-orphan")

    likes = db.relationship(Like, backref='publication_like', lazy='dynamic', cascade='all, delete-orphan', passive_deletes=True)
    comment = db.relationship(Comment, backref='publication_comment', lazy='dynamic', cascade='all, delete-orphan', passive_deletes=True)
    viewing = db.relationship(Viewing, backref='publication_viewing', lazy='dynamic', cascade='all, delete-orphan', passive_deletes=True)

    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    hashtags = db.Column(db.String(255), nullable=True)
    is_published = db.Column(db.Boolean, default=False)  # Черновик или опубликовано
    location = db.Column(db.String(255), nullable=True)  # Геолокация
    mentions = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def like_count(self):
        return self.likes.count()

    def comment_count(self):
        return self.comment.count()

    def view_count(self):
        return self.viewing.count()

    def publish(self):
        self.is_published = True
        self.updated_at = datetime.now()
        db.session.commit()

    def record_view(self, user_id):
        existing_view = Viewing.query.filter_by(user=user_id, publication=self.id).first()
        if not existing_view:
            new_view = Viewing(user=user_id, publication=self.id)
            db.session.add(new_view)
            db.session.commit()

    def get_viewers(self):
        return Viewing.query.filter_by(publication_id=self.id).all()


class PublicImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id', ondelete='CASCADE'))  # Ссылка на публикацию

class PublicVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(255))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id', ondelete='CASCADE'))  # Ссылка на публикацию

class PublicAudio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audio = db.Column(db.String(255))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id', ondelete='CASCADE'))  # Ссылка на публикацию
