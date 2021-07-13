from django.core.management.base import BaseCommand

from courses.models import Course


class Command(BaseCommand):
    help = 'Command for generation courses'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            default=10,
            help=u'Number of courses to create')

    def handle(self, *args, **options):
        count = options['count']
        out_str = f'Generated {count} courses:\n'
        for num, course in enumerate(Course.generate_courses(count), 1):
            out_str += f'{num}. {course}\n'

        self.stdout.write(self.style.SUCCESS(out_str))
