import os


class Config():
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/media/avatar/'
    UPLOAD_PATH_PUBLICATION_IMAGE = '/media/publication_image/'
    UPLOAD_PATH_PUBLICATION_VIDEO = '/media/publication_video/'
    UPLOAD_PATH_PUBLICATION_AUDIO = '/media/publication_audio/'
    UPLOAD_PATH_ACTUAL_IMAGE = '/media/actual_image/'
    UPLOAD_PATH_ACTUAL_VIDEO = '/media/actual_video/'
    UPLOAD_PATH_ACTUAL_AUDIO = '/media/actual_audio/'
    UPLOAD_PATH_ACTUAL = '/media/actual/'
    SERVER_PATH_AVATAR = ROOT + UPLOAD_PATH
    SERVER_PATH_PUBLICATION_IMAGE = ROOT + UPLOAD_PATH_PUBLICATION_IMAGE
    SERVER_PATH_PUBLICATION_VIDEO = ROOT + UPLOAD_PATH_PUBLICATION_VIDEO
    SERVER_PATH_PUBLICATION_AUDIO = ROOT + UPLOAD_PATH_PUBLICATION_AUDIO
    SERVER_PATH_ACTUAL_IMAGE = ROOT + UPLOAD_PATH_ACTUAL_IMAGE
    SERVER_PATH_ACTUAL_VIDEO = ROOT + UPLOAD_PATH_ACTUAL_VIDEO
    SERVER_PATH_ACTUAL_AUDIO = ROOT + UPLOAD_PATH_ACTUAL_AUDIO
    SERVER_PATH_ACTUAL = ROOT + UPLOAD_PATH_ACTUAL

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'shahzod9966636043@gmail.com'
    MAIL_DEFAULT_SENDER = 'shahzod9966636043@gmail.com'
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    import os

    SQLALCHEMY_DATABASE_URI = f"sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # USER = os.environ.get('POSTGRES_USER', 'shahzod008')
    # PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'Shahzod2008')
    # HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    # PORT = os.environ.get('POSTGRES_PORT', 5432)
    # DB = os.environ.get('POSTGRES_DB', 'db')
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = os.environ.get('SECRET_KEY', 'kjkfhbiuwlf2#R$T%$Y#W$F%$^heytg$^$%EW$GTFd2|2d#@|fd|@#d/342wed353w4TF%$3ewgf')
