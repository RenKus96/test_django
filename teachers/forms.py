# import datetime
import re

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm
import django_filters

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'phone_number',
            'years_of_experience',
            'academic_degrees',
            'group',
        ]
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'})
        }


    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result


    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result


    def clean_phone_number(self):
        if self.cleaned_data['phone_number']:
            return re.sub('[^+0-9]','',self.cleaned_data['phone_number'])
        else: 
            return self.cleaned_data['phone_number']
        # result = re.sub('[^+0-9]','',self.cleaned_data['phone_number'])
        # if Teacher.objects.filter(phone_number=result).exclude(id=self.instance.id).exists():
        #     raise ValidationError('The phone number already exists. Please try another one.')
        # return result


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    pass


class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'startswith'],
            'last_name': ['exact', 'startswith'],
            'academic_degrees': ['exact', 'startswith'],
            'group': ['exact'],
        }
