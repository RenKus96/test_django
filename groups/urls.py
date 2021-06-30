from groups.views import get_groups, create_group, update_group, delete_group
from django.urls import path

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:id>/', update_group, name='update'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]