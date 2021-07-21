from django.urls import path

from teachers.views import get_teachers, create_teacher, delete_teacher, generate_teachers, update_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:id>/', update_teacher, name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
    path('generate_teachers/', generate_teachers, name='generate'),
]