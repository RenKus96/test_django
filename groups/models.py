import datetime
import random

from django.db import models

from faker import Faker

GROUP_SUBJECT = [
    'Разработка web-приложений',
    'Разработка desktop-приложений',
    'Разработка серверных приложений',
    'Разработка мобильных приложений',
    'Программирование встраиваемых систем',
    'Системное программирование',
    'Разработка игр'
]


# Create your models here.
class Group(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    group_number = models.IntegerField(null=False)
    academic_subject = models.CharField(max_length=80, null=False)
    date_of_creation = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    headman = models.OneToOneField(
        # Student,
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )


    def __str__(self):
        # return f'№{self.group_number}, Курс: "{self.academic_subject}", \
        #     Дата создания: {self.date_of_creation}, \
        #     Кол-во студентов: {self.number_of_students}'
        return f'Group №{self.group_number} Created: {self.date_of_creation}'

    @staticmethod
    def generate_groups(count):
        faker = Faker()
        create_group = []
        for _ in range(count):
            grp = Group(
                group_number=faker.random_int(min=1, max=100),
                # academic_subject=faker.sentence(
                #     ext_word_list=GROUP_SUBJECT,
                #     nb_words=1
                # ),
                academic_subject=random.choice(GROUP_SUBJECT),
                date_of_creation=faker.date_this_year(),
                number_of_students=faker.random_int(min=1, max=30)
            )
            grp.save()
            create_group.append(str(grp))
        return create_group
