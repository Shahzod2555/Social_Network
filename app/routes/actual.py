from ..functions import save_image, save_media
from ..model.actual import ActualImage, ActualVideo, ActualAudio, Actual
from flask import Blueprint, render_template, redirect, request, flash
from flask_login import login_required, current_user
from ..forms import ActualAdd
from ..extentions import db


actual = Blueprint('actual_blueprint', __name__)


@actual.route('/actual-create', strict_slashes=False, methods=['POST', 'GET'])
@login_required
def add_actual():
    form = ActualAdd()

    if form.validate_on_submit():
        try:
            new_actual = Actual(description=form.description.data, author_id=current_user.id, image=save_image(form.images_.data))
            db.session.add(new_actual)
            db.session.commit()

            for image in form.images.data:
                if image:
                    new_image = ActualImage(image=save_media(image, "SERVER_PATH_ACTUAL_IMAGE"), actual_id=new_actual.id, author_id=current_user.id)
                    db.session.add(new_image)

            for video in form.videos.data:
                if video:
                    new_video = ActualVideo(video=save_media(video, "SERVER_PATH_ACTUAL_VIDEO"), actual_id=new_actual.id, author_id=current_user.id)
                    db.session.add(new_video)

            for audio in form.audios.data:
                if audio:
                    new_audio = ActualAudio(audio=save_media(audio, "SERVER_PATH_ACTUAL_AUDIO"), actual_id=new_actual.id, author_id=current_user.id)
                    db.session.add(new_audio)

            db.session.commit()
            return redirect(request.referrer or "/")

        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при создании публикации: {e}")
            flash("При создании публикации произошла ошибка", "danger")
            return redirect(request.referrer or "/")

    return render_template('actual/actual_add.html', form=form)
