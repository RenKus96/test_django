import datetime
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

# Create your models here.
from students.validators import adult_validator


class Student(models.Model):
    last_name = models.CharField(max_length=80, null=False, validators=[
        MinLengthValidator(2)
    ])
    first_name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(default=42)
    email = models.EmailField(max_length=120, null=True)
    birthdate = models.DateField(default=datetime.date.today, validators=[
        adult_validator
    ])
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}'

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
                birthdate=faker.date_between(start_date='-65y', end_date='-18y')
            )
            st.save()
            create_students.append(str(st))
        return create_students
