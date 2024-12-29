from flask import Blueprint, redirect, flash, request
from flask_login import login_required, current_user

from ..forms import CommentAdd
from ..extentions import db
from ..model.comment import Comment

comment_blueprint = Blueprint('comment_blueprint', __name__)

@comment_blueprint.route('/comment/<int:publication_id>', methods=['POST'])
@login_required
def comment(publication_id):
    form = CommentAdd()

    if form.validate_on_submit():
        new_comment = Comment(
            author=current_user.id,
            content=form.content.data,
            publication=publication_id
        )
        try:
            db.session.add(new_comment)
            db.session.commit()
            return redirect(request.referrer or "/")
        except Exception as e:
            flash("Ошибка при добавлении комментария", 'danger')
            print(f"Ошибка при создании публикации: {e}")
            return redirect(request.referrer or "/")

    return redirect(request.referrer or "/")