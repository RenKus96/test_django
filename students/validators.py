import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18
EMAIL_STOP_LIST = (
    'yandex.ru',
    'yandex.com',
    'yandex.ua',
    'ya.ru',
    'ya.ua',
    'ya.com',
    'mail.ru',
    'mail.ua',
    'inbox.ru',
    'list.ru',
    'bk.ru',
    'rambler.ru'
)


def adult_validator(birthdate):
    age = datetime.datetime.now().year - birthdate.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')

def email_stop_list_validator(email):
    if email.endswith(EMAIL_STOP_LIST):
        raise ValidationError('Данный почовый сервис запрещён в Украине')