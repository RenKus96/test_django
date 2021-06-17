# import datetime

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_number',
            'academic_subject',
            'date_of_creation',
            'number_of_students'
        ]
        # widgets = {
        #     'date_of_creation': DateInput(attrs={'type': 'date'})
        # }


class GroupCreateForm(GroupBaseForm):
    pass



