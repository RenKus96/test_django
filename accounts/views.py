from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy, reverse

from .forms import AccountRegistrationForm, AccountUpdateForm


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'User {self.request.user} has successfully logged in.')

        return result


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    # success_url = reverse_lazy('accounts:login')

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('password_change_done')


class AccountUpdateView(UpdateView):
    model = User
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('accounts:profile_update')
    form_class = AccountUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
