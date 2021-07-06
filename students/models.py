import datetime
from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from students.validators import AdultValidator, email_stop_list_validator
from groups.models import Group

class Student(models.Model):
    last_name = models.CharField(
        max_length=80, null=False, validators=[MinLengthValidator(2)
    ])
    first_name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(default=42)
    birthdate = models.DateField(
        # default=datetime.date.today, validators=[adult_validator]
        default=datetime.date.today, validators=[AdultValidator(21)]
    )
    email = models.EmailField(max_length=120, null=True, validators=[
        email_stop_list_validator
    ])
    phone_number = models.CharField(max_length=17, blank=True, unique=True, null=True)
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}, {self.group}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        create_students = []
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_between(
                    start_date='-65y',
                    end_date='-18y'
                )
            )
            st.age = relativedelta(datetime.date.today(), st.birthdate).years
            st.save()
            create_students.append(str(st))
        return create_students
