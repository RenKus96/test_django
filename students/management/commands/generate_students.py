from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Команда для генерация студентов'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            default=10,
            help=u'Количество создаваемых студентов')

    def handle(self, *args, **options):
        count = options['count']
        out_str = f'Сгенерировано {count} студентов:\n'
        for num, student in enumerate(Student.generate_students(count), 1):
            out_str += f'{num}. {student}\n'

        self.stdout.write(self.style.SUCCESS(out_str))
