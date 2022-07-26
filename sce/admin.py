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


@admin.register(Asignature)
class AsignatureAdmin(admin.ModelAdmin):
    fields = ['code', 'name', 'asignature_type',
            'department', 'is_active', 'is_exempted_interships']
    search_fields = ['code', 'name', 'department']
    list_display = ('id', 'code', 'name', 'asignature_type',
                    'department', 'is_active', 'is_exempted_interships',
                    'created_at', 'created_by', 'updated_at', 'updated_by')


admin.site.register(Pensum)


@admin.register(PensumDetail)
class PensumDetailAdmin(admin.ModelAdmin):
    fields = ['pensum', 'asignature', 'prelated_by', 'credits']
    # search_fields = ['name', 'id_document', 'department', 'gender']
    list_display = ['pensum', 'asignature', 'prelated_by', 'credits']
