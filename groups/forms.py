# import datetime

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm
import django_filters

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        # fields = [
        #     'group_number',
        #     'academic_subject',
        #     'date_of_creation',
        #     'end_date',
        #     'number_of_students',
        # ]
        fields = '__all__'
        widgets = {
            'date_of_creation': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ['end_date']


class GroupUpdateForm(GroupBaseForm):
    pass


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_number': ['exact'],
            # 'academic_subject': ['exact', 'icontains'],
            'course': ['exact'],
        }
