from django.urls import path

from courses.views import get_courses, create_course, update_course, delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:id>/', update_course, name='update'),
    path('delete/<int:pk>/', delete_course, name='delete'),
]