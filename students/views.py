from django.shortcuts import render
from django.http import HttpResponse
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields, validate, ValidationError
from students.models import Student
from students.utils import format_records


def hello(request):
    return HttpResponse('Hello')


@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def generate_students(request, count):
    out_str = f'Сгенерировано <b>{count}</b> студентов:<br>'
    for num, student in enumerate(Student.generate_students(count),1):
        out_str += f'<b>{num}.</b> {student}<br>'
    return HttpResponse(out_str)

@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "birthdate": fields.Date(
        required=False
    )},
    location="query"
)
def get_students(request, args):

    students = Student.objects.all()

    for param_name, param_value in args.items():
        students = students.filter(**{param_name: param_value})

        # if param_name == 'first_name':
        #     students = students.filter(first_name=param_value)
        # elif param_name == 'last_name':
        #     students = students.filter(last_name=param_value)

    records = format_records(students)

    return HttpResponse(records)