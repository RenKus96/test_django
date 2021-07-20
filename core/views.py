from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from students.forms import StudentUpdateForm
from students.models import Student


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )


class EditView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    def update_object(self, request, pk):
        student = self.model.objects.get(id=pk)

        if request.method == 'POST':
            form = self.form_class(instance=student, data=request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(self.success_url))
        else:
            form = self.form_class(instance=student)

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
