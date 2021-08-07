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
from django.urls import include, path

from core.views import index
# from groups.views import create_group, generate_groups, get_groups, update_group
# from students.views import create_student, generate_students, get_students, hello, update_student
# from teachers.views import create_teacher, generate_teachers, get_teachers, update_teacher
from groups.views import generate_groups
from students.views import generate_students, hello
from teachers.views import generate_teachers
from courses.views import generate_courses

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

	# path('generate_students/', generate_students),
    # path('students/', get_students),
    # path('students/create/', create_student),
    # path('students/update/<int:id>', update_student),
    path('students/', include('students.urls')),

    # path('generate_groups/', generate_groups),
	# path('groups/', get_groups),
    # path('groups/create/', create_group),
    # path('groups/update/<int:id>', update_group),
    path('groups/', include('groups.urls')),

    # path('generate_teachers/', generate_teachers),
	# path('teachers/', get_teachers),
    # path('teachers/create/', create_teacher),
    # path('teachers/update/<int:id>', update_teacher),
    path('teachers/', include('teachers.urls')),

    # path('generate_courses/', generate_courses),
    path('courses/', include('courses.urls')),

	path('__debug__/', include(debug_toolbar.urls)),    
]
