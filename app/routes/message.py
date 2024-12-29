from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from flask_socketio import emit, join_room
from ..extentions import db, socketio
from ..model.message import Message
from ..model.user import User

message_view = Blueprint('message_view', __name__)


@message_view.route('/chat/<int:recipient_id>')
@login_required
def chat(recipient_id):
    recipient = User.query.get_or_404(recipient_id)
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == recipient.id)) |
        ((Message.sender_id == recipient.id) & (Message.recipient_id == current_user.id))
    ).all()
    return render_template('chat/chat.html', recipient=recipient, messages=messages)


@socketio.on('send_private_message')
def handle_send_private_message(data):
    recipient_id = data['recipient_id']
    message_content = data['message']

    message = Message(sender_id=current_user.id, recipient_id=recipient_id, content=message_content, is_read=False)

    try:
        db.session.add(message)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        emit('error', {'error': str(e)}, room=current_user.id)
        return

    emit('receive_private_message', {'message': message_content, 'message_id': message.id}, room=recipient_id)

@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        join_room(current_user.id)

@message_view.route('/chats')
@login_required
def get_chats():
    user_chats = (
        db.session.query(User).join(
            Message,
            db.or_(
                Message.sender_id == User.id,
                Message.recipient_id == User.id
            )
        ).filter(
            db.or_(
                Message.sender_id == current_user.id,
                Message.recipient_id == current_user.id
            )
        ).filter(User.id != current_user.id)
    )

    count = 0
    for element in user_chats:
        count += 1

    return render_template('chat/chats.html', chats=user_chats, len_chats=count)


@socketio.on('delete_chat')
def handle_delete_chat(data):
    recipient_id = data['recipient_id']

    try:
        Message.query.filter(
            ((Message.sender_id == current_user.id) & (Message.recipient_id == recipient_id)) |
            ((Message.sender_id == recipient_id) & (Message.recipient_id == current_user.id))
        ).delete()
        db.session.commit()
        emit('chat_deleted', {'recipient_id': recipient_id}, room=request.sid)  # Уведомление конкретному пользователю
    except Exception as e:
        db.session.rollback()
        print(f"Ошибка при удалении чата: {e}")
        emit('error', {'error': 'Не удалось удалить чат'}, room=request.sid)