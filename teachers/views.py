from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  # noqa

from teachers.forms import TeacherCreateForm
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
    # "years_of_experience": fields.Int(
    #     required=False,
    #     validate=[validate.Range(min=1, max=60)]
    # ),
    "academic_degrees": fields.Str(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_value in args.items():
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})
    html_form = """
       <form method="get">
        <label >First name:</label>
        <input type="text" name="first_name"><br><br>

        <label >Last name:</label>
        <input type="text" name="last_name"><br><br>

        <label >Academic degrees:</label>
        <input type="text" name="academic_degrees"><br><br>

        <input type="submit" value="Search">
       </form>
    """
    records = format_records(teachers)
    response = html_form + records

    return HttpResponse(response)

@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """
    response = html_form
    return HttpResponse(response)

@csrf_exempt
def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeacherCreateForm(
            instance=teacher,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Save">
    </form>
    """
    response = html_form
    return HttpResponse(response)
