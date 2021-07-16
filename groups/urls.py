from django.urls import path

from groups.views import get_groups, create_group, delete_group, generate_groups, update_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:id>/', update_group, name='update'),
    path('delete/<int:pk>/', delete_group, name='delete'),
    path('generate_groups/', generate_groups, name='generate'),
]