from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from core.views import EditView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student
# from students.utils import format_records

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs


def hello(request):
    return HttpResponse('Hello')


@login_required 
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
    for num, student in enumerate(Student.generate(count), 1):
        out_str += f'<b>{num}.</b> {student}<br>'
    return HttpResponse(out_str)


# @use_args({
#     "first_name": fields.Str(
#         required=False
#     ),
#     "last_name": fields.Str(
#         required=False
#     ),
#     "birthdate": fields.Date(
#         required=False
#     )},
#     location="query"
# )
# def get_students(request, args):
#     students = Student.objects.all().select_related('group', 'headed_group')
#     obj_filter = StudentsFilter(data=request.GET, queryset=students)

#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={
#             'students': students,
#             'obj_filter': obj_filter,
#         }
#     )

# @login_required
# def create_student(request):
#     if request.method == 'GET':
#         form = StudentCreateForm()
#     elif request.method == 'POST':
#         form = StudentCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))

#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={
#             'form': form
#         }
#     )


# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     if request.method == 'GET':
#         form = StudentUpdateForm(instance=student)
#     elif request.method == 'POST':
#         form = StudentUpdateForm(
#             instance=student,
#             data=request.POST
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))

#     return render(
#         request=request,
#         template_name='students/update.html',
#         context={
#             'form': form
#         }
#     )


# def delete_student(request, pk):
#     student = get_object_or_404(Student, id=pk)
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))

#     return render(
#         request=request,
#         template_name='students/delete.html',
#         context={
#             'student': student
#         }
#     )


class StudentListView(LoginRequiredMixin, ListView):
    model = Student.objects.all().select_related('group', 'headed_group')
    template_name = 'students/list.html'

    def get_queryset(self):
        obj_filter = StudentsFilter(
            data=self.request.GET, 
            queryset=self.model
        )
        return obj_filter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_filter'] = self.get_queryset()
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'Student {self.object} was successfully added to base.')

        return result

# Вариант с вью в Core (не используется в URL)
# class UpdateStudentView(LoginRequiredMixin, EditView):
#     model = Student
#     form_class = StudentUpdateForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'

# А это Вариант с встроенной CBV (используется в URL)
class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
