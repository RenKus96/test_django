import datetime
from django.db import models

# Create your models here.
class Teachers(models.Model):
    last_name = models.CharField(max_length=80, null=False)
    first_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(default=datetime.date.today)
    email = models.EmailField(max_length=120, null=True)
    academic_subject = models.CharField(max_length=80, null=False)
    years_of_experience = models.IntegerField(default=0)
    academic_subject = models.CharField(max_length=80, null=False)
    academic_title = models.CharField(max_length=80, null=False)

    def __str__(self):
        return f'{self.academic_title}, {self.full_name()}, {self.academic_subject}, {self.id}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'
