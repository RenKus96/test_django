import datetime
from dateutil.relativedelta import relativedelta
import random

from django.db import models

from faker import Faker

# from students.validators import email_stop_list_validator
from groups.models import Group
from core.models import Person


ACADEMIC_DEGREES = [
    'ассистент', 'преподаватель', 'старший преподаватель',
    'доцент', 'профессор', 'заведующий кафедрой'
]


# Create your models here.
class Teacher(Person):
    years_of_experience = models.IntegerField(default=0)
    academic_degrees = models.CharField(max_length=80, null=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')

    def __str__(self):
        return f'{self.academic_degrees} {self.full_name()}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def _generate(cls):
        faker = Faker()
        obj = super()._generate()
        obj.years_of_experience=faker.random_int(min=1, max=60)
        obj.academic_degrees=random.choice(ACADEMIC_DEGREES)
        obj.save()
        return obj


    @classmethod
    def generate(cls, count):
        create_teachers = []
        for _ in range(count):
            create_teachers.append(str(cls._generate()))
        return create_teachers


    @staticmethod
    def generate_teachers(count):
        faker = Faker()
        create_teachers = []
        for _ in range(count):
            tchr = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                birthdate=faker.date_between(start_date='-80y', end_date='-20y'),
                email=faker.email(),
                years_of_experience=faker.random_int(min=1, max=60),
                academic_degrees=random.choice(ACADEMIC_DEGREES),
            )
            tchr.age = relativedelta(datetime.date.today(), tchr.birthdate).years
            tchr.save()
            create_teachers.append(str(tchr))
        return create_teachers
