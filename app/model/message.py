from ..extentions import db
from ..model.user import User
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор сообщения
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ID отправителя
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ID получателя
    content = db.Column(db.Text, nullable=False)  # Содержимое сообщения
    timestamp = db.Column(db.DateTime, default=datetime.now)  # Время отправки сообщения
    is_read = db.Column(db.Boolean, default=False)

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')  # Отношение к отправителю
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages')  # Отношение к получателю
