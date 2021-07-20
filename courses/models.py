import random

from django.db import models

from faker import Faker

GROUP_SUBJECT = [
    'Разработка web-приложений',
    'Разработка desktop-приложений',
    'Разработка серверных приложений',
    'Разработка мобильных приложений',
    'Программирование встраиваемых систем',
    'Системное программирование',
    'Разработка игр'
]


class Course(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    academic_subject = models.CharField(max_length=80, null=False)
    number_of_hours = models.IntegerField(default=10)


    def __str__(self):
        return f'{self.academic_subject} ({self.number_of_hours} hours)'

    @staticmethod
    def generate_courses(count):
        faker = Faker()
        create_course = []
        for _ in range(count):
            crs = Course(
                academic_subject=random.choice(GROUP_SUBJECT),
                number_of_hours=faker.random_int(min=1, max=30)
            )
            crs.save()
            create_course.append(str(crs))
        return create_course
