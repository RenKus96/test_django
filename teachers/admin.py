from django.contrib import admin

# Register your models here.
from teachers.models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'academic_degrees',
        'first_name',
        'last_name',
        'email',
    ]
    
    list_display_links = list_display
    list_per_page = 10

    fields = [
        ('first_name', 'last_name', 'birthdate'),
        ('email', 'phone_number'),
        ('years_of_experience', 'academic_degrees'),
        'group',
    ]

    search_fields = [
        'first_name',
        'last_name',
    ]

    list_filter = [
        'academic_degrees',
        'group',
    ]

admin.site.register(Teacher, TeacherAdmin)
