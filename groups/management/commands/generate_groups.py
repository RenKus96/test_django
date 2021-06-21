from django.core.management.base import BaseCommand

from groups.models import Group


class Command(BaseCommand):
    help = 'Команда для генерация групп'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            default=10,
            help=u'Количество создаваемых групп')

    def handle(self, *args, **options):
        count = options['count']
        out_str = f'Сгенерировано {count} групп:\n'
        for num, group in enumerate(Group.generate_groups(count), 1):
            out_str += f'{num}. {group}\n'

        self.stdout.write(self.style.SUCCESS(out_str))
