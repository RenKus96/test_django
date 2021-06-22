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
import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from groups.views import create_group, generate_groups, get_groups

from students.views import create_student, generate_students, get_students, hello, update_student

from teachers.views import create_teacher, generate_teachers, get_teachers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    
	path('generate_students/', generate_students),
    # path('students/', get_students),
    # path('students/create/', create_student),
    # path('students/update/<int:id>', update_student),
    path('students/', include('students.urls')),

	path('groups/', get_groups),
    path('groups/create/', create_group),
    path('generate_groups/', generate_groups),

	path('teachers/', get_teachers),
    path('teachers/create/', create_teacher),
    path('generate_teachers/', generate_teachers),

	path('__debug__/', include(debug_toolbar.urls)),    
]

urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]