import datetime
from dateutil.relativedelta import relativedelta

# from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

# from students.validators import AdultValidator, email_stop_list_validator
from groups.models import Group
from core.models import Person

class Student(Person):
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'


    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.save()
        return obj


    @classmethod
    def generate(cls, count):
        create_students = []
        for _ in range(count):
            create_students.append(str(cls._generate()))
        return create_students


    @staticmethod
    def generate_students(count):
        faker = Faker()
        create_students = []
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
                email=faker.email(),
            )
            st.age = relativedelta(datetime.date.today(), st.birthdate).years
            st.save()
            create_students.append(str(st))
        return create_students
