import os
from flask import current_app

import os.path
import secrets
from PIL import Image

from .model.like import Like
from .model.comment import Comment
from .model.publication import Publication
from flask_login import current_user


def delete_media_files(publication):
    # Удаляем изображения
    for image in publication.images:
        image_path = os.path.join(current_app.config['SERVER_PATH_PUBLICATION_IMAGE'], image.image)
        if os.path.exists(image_path):
            os.remove(image_path)
            print("все ок")

    # Удаляем видео
    for video in publication.videos:
        video_path = os.path.join(current_app.config['SERVER_PATH_PUBLICATION_VIDEO'], video.video)
        if os.path.exists(video_path):
            os.remove(video_path)
            print("все ок")


    # Удаляем аудио
    for audio in publication.audios:
        audio_path = os.path.join(current_app.config['SERVER_PATH_PUBLICATION_AUDIO'], audio.audio)
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print("все ок")

def save_media(media, folder):
    random_hex = secrets.token_hex(12)
    _, f_ext = os.path.splitext(media.filename)
    media_fn = random_hex + f_ext
    media_path = os.path.join(current_app.config[folder], media_fn)
    media.save(media_path)
    return media_fn

def save_ava_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH_AVATAR'], picture_fn)
    i = Image.open(picture)
    i.thumbnail((125, 125))
    i.save(picture_path)
    return picture_fn

def save_image(picture):
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = secrets.token_hex(12) + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH_ACTUAL'], picture_fn)
    i = Image.open(picture)
    i.thumbnail((150, 150))
    i.save(picture_path)
    return picture_fn

def get_publication_data(author_id=None, publications=None):
    if publications is None:
        if author_id is None:
            author_id = current_user.id
        publications = Publication.query.filter_by(
            author=author_id).order_by(
            Publication.updated_at.desc()).all()

    user_likes = {
        like.publication for like in Like.query.filter_by(
            author=current_user.id).all()}

    publication_comments = {
        publication.id: Comment.query.filter_by(
            publication=publication.id).order_by(
            Comment.created_at.desc()).all() for publication in publications}

    return publications, user_likes, publication_comments
