# Generated by Django 3.2.4 on 2021-06-13 17:16

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20210613_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduate_date2',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
