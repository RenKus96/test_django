# Generated by Django 3.2.4 on 2021-07-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_group_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='academic_subject',
        ),
    ]
