from django.urls import path

from teachers.views import get_teachers, create_teacher, update_teacher, delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:id>/', update_teacher, name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]