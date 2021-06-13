"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import hello, get_students, generate_students
from groups.views import get_groups, generate_groups
from teachers.views import get_teachers, generate_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('get_students/', get_students),
    path('generate_students/', generate_students),
    path('get_groups/', get_groups),
    path('generate_groups/', generate_groups),
    path('get_teachers/', get_teachers),
    path('generate_teachers/', generate_teachers)
]
