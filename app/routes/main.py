from ..forms import CommentAdd
from sqlalchemy.sql.expression import func
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ..functions import get_publication_data
from ..model.publication import Publication

main = Blueprint('main_blueprint', __name__)


@main.route('/')
@login_required
def index():
    publications = Publication.query.filter_by(is_published=True).order_by(func.random()).all()

    for publication in publications:
        publication.record_view(user_id=current_user.id)

    publications1, user_likes, publication_comments = get_publication_data(publications=publications)

    return render_template(
        'main/index.html',
        publications=publications,
        user_likes=user_likes,
        form=CommentAdd(),
        publication_comment=publication_comments,
        author=current_user,
    )
