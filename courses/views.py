from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from courses.forms import CourseCreateForm, CourseUpdateForm, CoursesFilter
from courses.models import Course

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs


@login_required 
@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def generate_courses(request, count):
    out_str = f'Generated <b>{count}</b> courses:<br>'
    for num, course in enumerate(Course.generate_courses(count), 1):
        out_str += f'<b>{num}.</b> {course}<br>'
    return HttpResponse(out_str)


# @use_args({
#     "academic_subject": fields.Str(
#         required=False
#     ),
#     "number_of_hours": fields.Int(
#         required=False,
#         missing=10
#     )},
#     location="query"
# )
# def get_courses(request, args):
#     courses = Course.objects.all().select_related('course_group')

#     obj_filter = CoursesFilter(data=request.GET, queryset=courses)
#     return render(
#         request=request,
#         template_name='courses/list.html',
#         context={
#             'courses': courses,
#             'obj_filter': obj_filter,
#         }
#     )


# def create_course(request):
#     if request.method == 'GET':
#         form = CourseCreateForm()
#     elif request.method == 'POST':
#         form = CourseCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#     return render(
#         request=request,
#         template_name='courses/create.html',
#         context={
#             'form': form
#         }
#     )

# def update_course(request, id):
#     course = get_object_or_404(Course, id=id)
#     if request.method == 'GET':
#         form = CourseUpdateForm(instance=course)
#     elif request.method == 'POST':
#         form = CourseUpdateForm(
#             instance=course,
#             data=request.POST
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#     return render(
#         request=request,
#         template_name='courses/update.html',
#         context={
#             'form': form,
#             'course': course,
#         }
#     )


# def delete_course(request, pk):
#     course = get_object_or_404(Course, id=pk)
#     if request.method == 'POST':
#         course.delete()
#         return HttpResponseRedirect(reverse('courses:list'))

#     return render(
#         request=request,
#         template_name='courses/delete.html',
#         context={
#             'course': course
#         }
#     )


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/list.html'
    paginate_by = 10

    def get_filter(self):
        return CoursesFilter(
            data=self.request.GET, 
            queryset=self.model.objects.all().select_related('course_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_filter'] = self.get_filter()
        return context


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
