from flask import Blueprint, redirect, request
from flask_login import login_required, current_user

from ..extentions import db
from ..model.like import Like

like_blueprint = Blueprint('like_blueprint', __name__)

@like_blueprint.route('/like/<int:publication_id>', methods=['POST', 'GET'])
@login_required
def like(publication_id):
    author = current_user.id

    existing_like = Like.query.filter_by(author=author, publication=publication_id).first()

    try:
        if existing_like:
            db.session.delete(existing_like)
            db.session.commit()
        else:
            new_like = Like(author=author, publication=publication_id)
            db.session.add(new_like)
            db.session.commit()
    except Exception as e:
        print(f"Ошибка при создании публикации: {e}")

    return redirect(request.referrer or "/")
