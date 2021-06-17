from django.http import HttpResponse
from django.shortcuts import render  # noqa

from groups.models import Group
from groups.utils import format_records

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
def generate_groups(request, count):
    out_str = f'Сгенерировано <b>{count}</b> групп:<br>'
    for num, group in enumerate(Group.generate_groups(count), 1):
        out_str += f'<b>{num}.</b> {group}<br>'
    return HttpResponse(out_str)


@use_args({
    "group_number": fields.Int(
        required=False,
        validate=[validate.Range(min=1, max=100)]
    ),
    "academic_subject": fields.Str(
        required=False
    ),
    "date_of_creation": fields.Date(
        required=False
    )},
    location="query"
)
def get_groups(request, args):
    groups = Group.objects.all()
    for param_name, param_value in args.items():
        groups = groups.filter(**{param_name: param_value})
    records = format_records(groups)
    return HttpResponse(records)
