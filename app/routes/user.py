from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from ..forms import CommentAdd, UpdateAccount
from ..model.user import User
from ..functions import get_publication_data, save_ava_picture
from ..extentions import db

user = Blueprint('user_blueprint', __name__)

@user.route('/profile/', strict_slashes=False)
@login_required
def profile():
    us = User.query.all()
    publications, user_likes, publication_comments = get_publication_data()

    us_ac = User.query.get(current_user.id)
    actual_all = us_ac.actual

    return render_template(
        'user/profile.html',
        publications=publications,
        us=us,
        user_likes=user_likes,
        form=CommentAdd(),
        actual_all=actual_all,
        publication_comment=publication_comments,
        author=current_user,
        subscription_count=current_user.subscription_count(),
        subscribers_count=current_user.subscribers_count(),
        publication_count=current_user.publication_count()
    )


@user.route('/user/<int:user_id>')
@login_required
def user_profile(user_id):
    publications, user_likes, publication_comments = get_publication_data(author_id=user_id)
    user_us = User.query.get_or_404(user_id)

    if user_id == current_user.id:
        return redirect(url_for('user_blueprint.profile'))

    return render_template(
        'user/user.html',
        publications=publications,
        user_likes=user_likes,
        form=CommentAdd(),
        publication_comment=publication_comments,
        author=user_us,
        subscription_count=user_us.subscription_count(),
        subscribers_count=user_us.subscribers_count(),
        publication_count=user_us.publication_count()
    )


@user.route('/user/delete/account')
@login_required
def delete_account():
    try:
        db.session.delete(User.query.filter_by(id=current_user.id).first())
        db.session.commit()
        next_page = request.referrer
        return redirect(next_page) if next_page else redirect('/'), flash("Аккаунт успешно удален", "success")
    except Exception as e:
        print(e)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect('/'), flash("Что-то пошло не так!", "danger")


@user.route('/user/update/account', methods=['GET', 'POST'])
@login_required
def update_account():
    us = User.query.filter_by(id=current_user.id).first()
    form = UpdateAccount()

    if request.method == 'GET':
        form.login.data = us.username
        form.phone.data = us.phone
        form.bio.data = us.bio
        form.last_name.data = us.last_name
        form.middle_name.data = us.middle_name
        form.first_name.data = us.first_name


    if form.validate_on_submit():
        try:
            us.username = form.login.data
            us.phone = form.phone.data
            us.bio = form.bio.data
            us.last_name = form.last_name.data
            us.middle_name = form.middle_name.data
            us.first_name = form.first_name.data

            if form.avatar.data:
                us.avatar = save_ava_picture(form.avatar.data)
            db.session.commit()
            return redirect(request.referrer), flash("Данные успешно изменены", "success")
        except Exception as e:
            print(e)
            db.session.rollback()
    return render_template(template_name_or_list='user/update_account.html', form=form)


@user.route('/user/delete/avatar')
@login_required
def delete_avatar():
    try:
        User.query.filter_by(id=current_user.id).first().avatar = "ava.svg"
        db.session.commit()
        next_page = request.referrer
        return redirect(next_page) if next_page else redirect('/'), flash("Аватарка удалена", "success")
    except Exception as e:
        print(e)
        db.session.rollback()
        next_page = request.referrer
        return redirect(next_page) if next_page else redirect('/'), flash("Аватарку удалить не получилось.", "danger")

