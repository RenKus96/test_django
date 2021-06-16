import datetime
import random

from django.db import models

from faker import Faker

ACADEMIC_DEGREES = [
    'ассистент', 'преподаватель', 'старший преподаватель',
    'доцент', 'профессор', 'заведующий кафедрой'
]


# Create your models here.
class Teacher(models.Model):
    last_name = models.CharField(max_length=80, null=False)
    first_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(default=datetime.date.today)
    email = models.EmailField(max_length=120, null=True)
    years_of_experience = models.IntegerField(default=0)
    academic_degrees = models.CharField(max_length=80, null=False)

    def __str__(self):
        return f'{self.academic_degrees} {self.full_name()}, \
            email:{self.email}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def generate_teachers(count):
        faker = Faker()
        create_teachers = []
        for _ in range(count):
            tchr = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                birthdate=faker.date_between(
                    start_date='-80y',
                    end_date='-20y'
                ),
                email=faker.email(),
                years_of_experience=faker.random_int(min=1, max=60),
                academic_degrees=random.choice(ACADEMIC_DEGREES)
            )
            tchr.save()
            create_teachers.append(str(tchr))
        return create_teachers
