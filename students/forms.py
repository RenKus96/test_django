# import datetime
# from dateutil.relativedelta import relativedelta
import re

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm
import django_filters

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'birthdate',
            'email',
            'phone_number',
            'enroll_date',
            'graduate_date',
            'graduate_date2',
            'group',
        ]
        # fields = '__all__'
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
            'enroll_date': DateInput(attrs={'type': 'date'}),
            'graduate_date': DateInput(attrs={'type': 'date'}),
            'graduate_date2': DateInput(attrs={'type': 'date'}),
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
        # if Student.objects.filter(phone_number=result).exclude(id=self.instance.id).exists():
        #     raise ValidationError('The phone number already exists. Please try another one.')
        # return result


    # def clean_birthdate(self):
    #     birthdate = self.cleaned_data['birthdate']
    #     age = datetime.datetime.now().year - birthdate.year
    #     if age < 18:
    #         raise ValidationError('Age should be greater than 18 y.o.')
    #
    #     return birthdate


    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = ['age']
    # class Meta(StudentBaseForm.Meta):
    #     fields = [
    #         'first_name',
    #         'last_name',
    #         'age',
    #         'birthdate',
    #         'email',
    #         'phone_number',
    #         'enroll_date',
    #         'graduate_date',
    #         'graduate_date2',
    #         'group',
    #     ]


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['gt', 'lt',],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
            'group': ['exact'],
        }
