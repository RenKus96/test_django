from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  # noqa

from groups.forms import GroupCreateForm
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


@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """
    response = html_form
    return HttpResponse(response)
