from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group
from students.models import Student
# from groups.utils import format_records

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
def generate_groups(request, count):
    out_str = f'Сгенерировано <b>{count}</b> групп:<br>'
    for num, group in enumerate(Group.generate_groups(count), 1):
        out_str += f'<b>{num}.</b> {group}<br>'
    return HttpResponse(out_str)


# @use_args({
#     "group_number": fields.Int(
#         required=False,
#         validate=[validate.Range(min=1, max=100)]
#     ),
#     # "academic_subject": fields.Str(
#     #     required=False
#     # ),
#     "date_of_creation": fields.Date(
#         required=False
#     )},
#     location="query"
# )
# def get_groups(request, args):
#     groups = Group.objects.all().select_related('course', 'headman')
#     obj_filter = GroupsFilter(data=request.GET, queryset=groups)
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={
#             # 'groups': groups,
#             'obj_filter': obj_filter,
#         }
#     )


# def create_group(request):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#     elif request.method == 'POST':
#         form = GroupCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     return render(
#         request=request,
#         template_name='groups/create.html',
#         context={
#             'form': form
#         }
#     )

# def update_group(request, pk):
#     group = get_object_or_404(Group, id=pk)
#     if request.method == 'GET':
#         form = GroupUpdateForm(instance=group)
#     elif request.method == 'POST':
#         form = GroupUpdateForm(
#             instance=group,
#             data=request.POST
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     return render(
#         request=request,
#         template_name='groups/update.html',
#         context={
#             'form': form,
#             # 'group': group,
#             'students': group.students.select_related('group',  'headed_group').all(),
#             'teachers': group.teachers.select_related('group').all(),
#         }
#     )


# def delete_group(request, pk):
#     group = get_object_or_404(Group, id=pk)
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('groups:list'))

#     return render(
#         request=request,
#         template_name='groups/delete.html',
#         context={
#             'group': group
#         }
#     )


class GroupListView(LoginRequiredMixin, ListView):
    model = Group.objects.all().select_related('course', 'headman').prefetch_related('students', 'teachers')
    queryset = GroupsFilter(queryset=model)
    template_name = 'groups/list.html'

    def get_queryset(self):
        obj_filter = GroupsFilter(
            data=self.request.GET, 
            queryset=self.model
        )
        return obj_filter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_filter'] = self.get_queryset()
        return context


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    # pk_url_kwarg = 'ppk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.select_related('group', 'headed_group').all()
        context['teachers'] = self.get_object().teachers.select_related('group').all()

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError as ex:
            pass

        return initial

    def form_valid(self, form):
        respose = super().form_valid(form)
        form.instance.headman = Student.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return respose


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
    