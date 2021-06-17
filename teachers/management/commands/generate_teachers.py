from django.core.management.base import BaseCommand

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Команда для генерация преподавателей'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            default=10,
            help=u'Количество создаваемых преподавателей')

    def handle(self, *args, **options):
        count = options['count']
        out_str = f'Сгенерировано {count} преподавателей:\n'
        for num, teacher in enumerate(Teacher.generate_teachers(count), 1):
            out_str += f'{num}. {teacher}\n'
        self.stdout.write(self.style.SUCCESS(out_str))
