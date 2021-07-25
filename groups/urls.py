from django.urls import path

from groups.views import get_groups, create_group, delete_group, generate_groups, update_group
from groups.views import GroupCreateView, GroupDeleteView, GroupListView, GroupUpdateView

app_name = 'groups'

urlpatterns = [
    # path('', get_groups, name='list'),
    # path('create/', create_group, name='create'),
    # path('update/<int:pk>/', update_group, name='update'),
    # path('delete/<int:pk>/', delete_group, name='delete'),
    path('', GroupListView.as_view(), name='list'),
    path('create/', GroupCreateView.as_view(), name='create'),
    path('update/<int:ppk>/', GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='delete'),
    path('generate_groups/', generate_groups, name='generate'),
]

