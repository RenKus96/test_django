from django.urls import path

# from teachers.views import get_teachers, create_teacher, delete_teacher, generate_teachers, update_teacher
from teachers.views import generate_teachers, TeacherCreateView, TeacherDeleteView, TeacherListView, TeacherUpdateView

app_name = 'teachers'

urlpatterns = [
    # path('', get_teachers, name='list'),
    # path('create/', create_teacher, name='create'),
    # path('update/<int:id>/', update_teacher, name='update'),
    # path('delete/<int:pk>/', delete_teacher, name='delete'),
    path('', TeacherListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete'),
    path('generate_teachers/', generate_teachers, name='generate'),


]