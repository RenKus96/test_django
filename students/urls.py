from django.urls import path

from students.views import get_students, create_student, delete_student, generate_students, update_student
from students.views import UpdateStudentView, StudentUpdateView

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    # path('update/<int:id>/', update_student, name='update'),
    # path('update/<int:pk>/', UpdateStudentView.update_object, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
    path('generate_students/', generate_students, name='generate'),

]