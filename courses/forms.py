from django.forms import ModelForm
import django_filters

from courses.models import Course


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateForm(CourseBaseForm):
    pass


class CourseUpdateForm(CourseBaseForm):
    pass


class CoursesFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'academic_subject': ['exact', 'icontains'],
            'number_of_hours': ['gt', 'lt',],
        }
