from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


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

    @classmethod
    def update_object(self, request, pk):
        update_obj = self.model.objects.get(id=pk)

        if request.method == 'POST':
            form = self.form_class(instance=update_obj, data=request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(self.success_url))
        else:
            form = self.form_class(instance=update_obj)

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
