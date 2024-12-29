from flask_wtf.file import FileAllowed
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, EmailField, PasswordField, SubmitField, TextAreaField, FileField, BooleanField, MultipleFileField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
from flask_wtf import FlaskForm


class EmailForm(FlaskForm):
    email = EmailField(label='Электронная почта', validators=[DataRequired()])
    submit = SubmitField('Получить код')


class CodForm(FlaskForm):
    cod = IntegerField(
        label='Введите полученный код',
        validators=[
            DataRequired()])
    submit = SubmitField('Подтвердить почту')


class RegistrationForm(FlaskForm):
    login = StringField(
        label='Логин',
        validators=[
            DataRequired(message="Придумай логин."),
            Length(min=5, max=50, message="Логин должен быть от 5 до 50 символов.")
        ],
        render_kw={"placeholder": "Введите логин", "autocomplete": "username"}
    )
    phone = StringField(
        label='Номер телефона',
        validators=[
            DataRequired(
                message="Введи номер телефона, в формате +7-999-999-99-99"),
            Length(
                min=11,
                max=12,
                message="Номер телефона должен быть от 10 до 15 цифр."),
            Regexp(
                regex=r'^\+?1?\d{9,15}$',
                message="Номер телефона должен содержать только цифры.")],
        render_kw={
            "placeholder": "Введите номер телефона",
            "autocomplete": "tel"})
    password = PasswordField(
        label='Пароль',
        validators=[
            DataRequired(
                message="Придумай пароль."),
            Regexp(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%_/\-.,|:;}{\[\]><~`*?&])[A-Za-z\d@$!%_/\-.,|:;}{\[\]><~`*?&]{8,}$',
                message="Пароль должен содержать минимум одну заглавную букву, одну цифру и один специальный символ (@$!%*?&)."),
            Length(
                min=8,
                message="Ваш пароль должен содержать не менее 8 символов")],
        render_kw={
            "placeholder": "Введите пароль",
            "autocomplete": "new-password"})
    confirm_password = PasswordField(
        label='Подтвердите пароль',
        validators=[
            DataRequired(message="Подтверди пароль"),
            EqualTo('password', message='Пароли должны совпадать')
        ],
        render_kw={"placeholder": "Повторите пароль", "autocomplete": "new-password"}
    )
    avatar = FileField(
        label="Аватарка",
        validators=[
            FileAllowed(
                upload_set=[
                    'png',
                    'jpeg',
                    'jpg'],
                message="Допустимы только изображения в форматах PNG, JPEG, JPG.")])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    password = PasswordField(
        label='Пароль',
        name="password",
        validators=[
            DataRequired(
                message="Введите пароль")],
        render_kw={
            "placeholder": "Введите пароль",
            "autocomplete": "new-password"})
    login = StringField(
        name="login",
        label='Логин', validators=[
            DataRequired(
                message="Введите логин"), Length(
                min=5, max=50, message="Логин должен быть от 5 до 50 символов.")], render_kw={
                    "placeholder": "Введите логин", "autocomplete": "username"})
    submit = SubmitField('Войти')


class CommentAdd(FlaskForm):
    content = TextAreaField(label='Комментарий', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class UpdateAccount(FlaskForm):
    login = StringField(
        label='Логин',
        validators=[
            DataRequired(message="Придумай логин."),
            Length(min=5, max=50, message="Логин должен быть от 5 до 50 символов.")
        ],
        render_kw={"placeholder": "Введите логин", "autocomplete": "username"}
    )
    first_name = StringField(
        label='Имя',
        render_kw={"placeholder": "Имя", "autocomplete": "name_first"}
    )
    last_name = StringField(
        label='Фамилия',
        render_kw={"placeholder": "Фамилия", "autocomplete": "name_last"}
    )
    middle_name = StringField(
        label='Отчество',
        render_kw={"placeholder": "Отчество", "autocomplete": "name_middle"}
    )
    bio = StringField(
        label='Биография',
        render_kw={"placeholder": "Пару слов туда сюда"}
    )
    phone = StringField(
        label='Номер телефона',
        validators=[
            DataRequired(
                message="Введи номер телефона, в формате +7-999-999-99-99"),
            Length(
                min=11,
                max=12,
                message="Номер телефона должен быть от 10 до 15 цифр."),
            Regexp(
                regex=r'^\+?1?\d{9,15}$',
                message="Номер телефона должен содержать только цифры.")],
        render_kw={
            "placeholder": "Введите номер телефона",
            "autocomplete": "tel"}
    )
    avatar = FileField(
        label="Аватарка",
        validators=[
            FileAllowed(
                upload_set=[
                    'png',
                    'jpeg',
                    'jpg'],
                message="Допустимы только изображения в форматах PNG, JPEG, JPG.")])

    submit = SubmitField('Сохранить')


class PublicationCreate(FlaskForm):
    title = StringField(label='Заголовок', validators=[DataRequired(), Length(max=255)])
    content = TextAreaField(label='Статья')
    hashtags = StringField(label='Хештеги')
    is_publication = BooleanField(default=True, label="Публиковать?")
    images = MultipleFileField(label='Фотки', validators=[FileAllowed(['png', 'jpeg', 'jpg'])])
    videos = MultipleFileField(label='Видео', validators=[FileAllowed(['mp4', 'mov'])])
    audios = MultipleFileField(label='Аудио', validators=[FileAllowed(['mp3', 'mov'])])
    location = StringField(label='Локация')
    mentions = StringField(label='Упомянуть пользователя')
    submit = SubmitField('Создать публикацию')


class PublicationUpdate(FlaskForm):
    title = StringField(label='Заголовок', validators=[DataRequired(), Length(max=255)])
    content = TextAreaField(label='Статья')
    hashtags = StringField(label='Хештеги')
    is_publication = BooleanField(default=True)
    image = FileField(label='Фотки', validators=[FileAllowed(['png', 'jpeg', 'jpg'])])
    video = FileField(label='Видео', validators=[FileAllowed(['mp4', 'mov'])])
    audio = FileField(label='Аудио', validators=[FileAllowed(['mp3', 'mov'])])
    location = StringField(label='Локация')
    mentions = StringField(label='Упомянуть пользователя')
    submit = SubmitField('Обновить публикацию')


class ActualAdd(FlaskForm):
    is_publication = BooleanField(default=True, label="Публиковать?")
    description = StringField(label='Пару слов туда сюда')
    mentions = StringField(label='Упомянуть пользователя')
    location = StringField(label='Локация')
    images_ = FileField(label='Фотка для обложки', validators=[FileAllowed(['png', 'jpeg', 'jpg'])])
    images = MultipleFileField(label='Фотки', validators=[FileAllowed(['png', 'jpeg', 'jpg'])])
    videos = MultipleFileField(label='Видео', validators=[FileAllowed(['mp4', 'mov'])])
    audios = MultipleFileField(label='Аудио', validators=[FileAllowed(['mp3', 'mov'])])
    submit = SubmitField('Создать актуалочку')

