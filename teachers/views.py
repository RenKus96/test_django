from django.http import HttpResponse
# from django.shortcuts import render

from teachers.models import Teacher
from teachers.utils import format_records

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs


@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def generate_teachers(request, count):
    out_str = f'Сгенерировано <b>{count}</b> преподавателей:<br>'
    for num, teacher in enumerate(Teacher.generate_teachers(count), 1):
        out_str += f'<b>{num}.</b> {teacher}<br>'
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
    ),
    "years_of_experience": fields.Int(
        required=False,
        validate=[validate.Range(min=1, max=60)]
    ),
    "academic_degrees": fields.Str(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})
    records = format_records(teachers)
    return HttpResponse(records)
