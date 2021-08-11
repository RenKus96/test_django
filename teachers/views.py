from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher
# from teachers.utils import format_records

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs
from copy import copy


@login_required 
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
    for num, teacher in enumerate(Teacher.generate(count), 1):
        out_str += f'<b>{num}.</b> {teacher}<br>'
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
#     ),
#     "academic_degrees": fields.Str(
#         required=False
#     )},
#     location="query"
# )
# def get_teachers(request, args):
#     teachers = Teacher.objects.all().select_related('group')
#     obj_filter = TeachersFilter(data=request.GET, queryset=teachers)
#     return render(
#         request=request,
#         template_name='teachers/list.html',
#         context={
#             # 'teachers': teachers,
#             'obj_filter': obj_filter,
#         }
#     )

# def create_teacher(request):
#     if request.method == 'GET':
#         form = TeacherCreateForm()
#     elif request.method == 'POST':
#         form = TeacherCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={
#             'form': form
#         }
#     )


# def update_teacher(request, id):
#     teacher = get_object_or_404(Teacher, id=id)
#     if request.method == 'GET':
#         form = TeacherUpdateForm(instance=teacher)
#     elif request.method == 'POST':
#         form = TeacherUpdateForm(
#             instance=teacher,
#             data=request.POST
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     return render(
#         request=request,
#         template_name='teachers/update.html',
#         context={
#             'form': form
#         }
#     )


# def delete_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:list'))

#     return render(
#         request=request,
#         template_name='teachers/delete.html',
#         context={
#             'teacher': teacher
#         }
#     )


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    paginate_by = 10

    def get_filter(self):
        return  TeachersFilter(
            data=self.request.GET, 
            queryset=self.model.objects.all().select_related('group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_filter'] = self.get_filter()
        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']
        context['get_params'] = params.urlencode()
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
