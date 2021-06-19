# import datetime

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'years_of_experience',
            'academic_degrees'
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


class TeacherCreateForm(TeacherBaseForm):
    pass



