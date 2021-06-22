import datetime

from django.core.exceptions import ValidationError

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


def adult_validator(birthdate, adult_age_limit = 18):
    age = datetime.datetime.now().year - birthdate.year
    if age < adult_age_limit:
        raise ValidationError(f'Age should be greater than {adult_age_limit} y.o.')


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, birthdate):
        adult_validator(birthdate, self.age_limit)

def email_stop_list_validator(email):
    if email.endswith(EMAIL_STOP_LIST):
        raise ValidationError('Данный почовый сервис запрещён в Украине')