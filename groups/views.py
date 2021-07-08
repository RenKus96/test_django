from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404  # noqa

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group
# from groups.utils import format_records

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
    # "group_number": fields.Int(
    #     required=False,
    #     validate=[validate.Range(min=1, max=100)]
    # ),
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
    # for param_name, param_value in args.items():
    #     if param_value:
    #         groups = groups.filter(**{param_name: param_value})
    obj_filter = GroupsFilter(data=request.GET, queryset=groups)
    return render(
        request=request,
        template_name='groups/list.html',
        context={
            # 'groups': groups,
            'obj_filter': obj_filter,
        }
    )


#@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'form': form
        }
    )

#@csrf_exempt
def update_group(request, id):
    # group = Group.objects.get(id=id)
    group = get_object_or_404(Group, id=id)
    if request.method == 'GET':
        form = GroupUpdateForm(instance=group)
    elif request.method == 'POST':
        form = GroupUpdateForm(
            instance=group,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'form': form,
            'group': group,
            # 'students': group.students.all(),
        }
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={
            'group': group
        }
    )
