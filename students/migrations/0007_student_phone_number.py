# Generated by Django 3.2.4 on 2021-06-22 14:46

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.EmailField(max_length=20, null=True, validators=[students.validators.phone_number_double_validator]),
        ),
    ]
