from django.urls import path

from students.views import generate_students
from students.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

app_name = 'students'

urlpatterns = [
    # path('', get_students, name='list'),
    # path('create/', create_student, name='create'),
    # path('update/<int:id>/', update_student, name='update'),
    # path('update/<int:pk>/', UpdateStudentView.update_object, name='update'),
    # path('delete/<int:pk>/', delete_student, name='delete'),
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('generate_students/', generate_students, name='generate'),

]