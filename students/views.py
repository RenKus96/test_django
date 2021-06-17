from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render

from students.forms import StudentCreateForm
from students.models import Student
from students.utils import format_records

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs


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
    for num, student in enumerate(Student.generate_students(count), 1):
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
    # Students = 42
    students = Student.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

    html_form = """
       <form method="get">
        <label >First name:</label>
        <input type="text" name="first_name"><br><br>

        <label >Last name:</label>
        <input type="text" name="last_name"><br><br>

        <label>Age:</label>
        <input type="number" name="age"><br><br>

        <input type="submit" value="Search">
       </form>
    """

    records = format_records(students)
    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_student(request):
    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """

    response = html_form

    return HttpResponse(response)


@csrf_exempt
def update_student(request, id_student):
    student = Student.objects.get(id=id_student)

    if request.method == 'GET':

        form = StudentCreateForm(instance=student)

    elif request.method == 'POST':

        form = StudentCreateForm(
            instance=student,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Save">
    </form>
    """

    response = html_form

    return HttpResponse(response)
