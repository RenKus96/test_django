# Generated by Django 3.2.4 on 2021-07-06 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=datetime.date.today, validators=[21]),
        ),
    ]
