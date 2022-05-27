from django.contrib import admin
from .models import *

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ['faculty', 'name']
    list_display = ('id', 'name', 'faculty', 'created_at', 'updated_at')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['school', 'name']
    search_fields = ['name']
    list_display = ('id', 'name', 'school', 'created_at', 'updated_at')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    fields = ['name', 'id_document', 'department', 'gender']
    search_fields = ['name', 'id_document', 'department', 'gender']
    list_display = ('id', 'name', 'id_document', 'department', 'gender', 'created_at', 'updated_at')
