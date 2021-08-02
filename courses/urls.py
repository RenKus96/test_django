from django.urls import path

from courses.views import generate_courses
from courses.views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'courses'

urlpatterns = [
    # path('', get_courses, name='list'),
    # path('create/', create_course, name='create'),
    # path('update/<int:id>/', update_course, name='update'),
    # path('delete/<int:pk>/', delete_course, name='delete'),
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
    path('generate_courses/', generate_courses, name='generate'),
]