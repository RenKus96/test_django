import datetime
from django.db import models

# Create your models here.
class Groups(models.Model):
    group_number = models.IntegerField(null=False)
    academic_subject = models.CharField(max_length=80, null=False)
    date_of_creation = models.DateField(default=datetime.date.today)
    number_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.group_number}, {self.academic_subject}, {self.number_of_students}'
