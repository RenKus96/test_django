from django.contrib import admin

# Register your models here.
from .models import Group
from students.models import Student
from teachers.models import Teacher


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthdate',
        'email',
    ]

    readonly_fields = fields
    show_change_link = True
    extra = 0

class TeachersInlineTable(admin.TabularInline):
    model = Teacher
    fields = [
        'academic_degrees',
        'first_name',
        'last_name',
        'email',
    ]

    readonly_fields = fields
    show_change_link = True
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_number',
        'course',
        'date_of_creation',
        'end_date',
        'number_of_students',
        'headman',
    ]
    
    list_display_links = list_display
    list_per_page = 10

    fields = [
        ('group_number',
        'course'),
        ('date_of_creation',
        'end_date'),
        ('number_of_students',
        'headman'),
    ]

    readonly_fields = ['course', 'headman']

    search_fields = [
        'group_number',
    ]

    list_filter = [
        'course',
    ]

    inlines = [StudentsInlineTable, TeachersInlineTable]

admin.site.register(Group, GroupAdmin)
