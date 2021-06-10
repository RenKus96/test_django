from django.core.management.base import BaseCommand, CommandError
from students.models import Student

class Command(BaseCommand):
    help = 'Команда для генерация студентов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help=u'Количество создаваемых студентов')

    def handle(self, *args, **options):
        count = options['count']
        out_str = f'Сгенерировано {count} студентов:\n'
        for num, student in enumerate(Student.generate_students(count),1):
            out_str += f'{num}. {student}\n'
        self.stdout.write(self.style.SUCCESS(out_str))