from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404  # noqa

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher
# from teachers.utils import format_records

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
    # for num, teacher in enumerate(Teacher.generate_teachers(count), 1):
    for num, teacher in enumerate(Teacher.generate(count), 1):
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
    "academic_degrees": fields.Str(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().select_related('group')
    # for param_name, param_value in args.items():
    #     if param_value:
    #         teachers = teachers.filter(**{param_name: param_value})
    obj_filter = TeachersFilter(data=request.GET, queryset=teachers)
    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            # 'teachers': teachers,
            'obj_filter': obj_filter,
        }
    )

#@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(
        request=request,
        template_name='teachers/create.html',
        context={
            'form': form
        }
    )


#@csrf_exempt
def update_teacher(request, id):
    # teacher = Teacher.objects.get(id=id)
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'GET':
        form = TeacherUpdateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeacherUpdateForm(
            instance=teacher,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(
        request=request,
        template_name='teachers/update.html',
        context={
            'form': form
        }
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/delete.html',
        context={
            'teacher': teacher
        }
    )
