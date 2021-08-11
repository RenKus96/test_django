from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Profile


class AccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class AccountUpdateForm(UserChangeForm):
    # Чтоб убрать с формы поле password, раскоментируйте строку ниже
    # password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AccountUpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'interests']

