from students.views import get_students, create_student, update_student, delete_student
from django.urls import path

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:id>/', update_student, name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]