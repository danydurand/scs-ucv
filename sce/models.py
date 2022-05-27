from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
)

STATUS_CHOICES = (
    ('A', 'ACTIVE'),
    ('I', 'INACTIVE'),
)

class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_faculties')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_faculties')
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('faculty-detail', kwargs={'pk': self.id})
        
    @property
    def school_qty(self):
        return self.schools.count()
    
    class Meta:
        # db_table = 'faculty'
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        ordering = ['name']


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='schools')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_schools')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_schools')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school-detail', kwargs={'pk': self.id})
        
    @property
    def department_qty(self):
        return self.departments.count()
    
    class Meta:
        # db_table = 'school'
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'
        ordering = ['name']


class Department(models.Model):
    name = models.CharField('Nombre', max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField('F. Creacion', auto_now_add=True)
    updated_at = models.DateTimeField('F. Modificacion', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_departments')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_departments')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.id})
        
    @property
    def professor_qty(self):
        return self.professors.count()
    
    class Meta:
        # db_table = 'deparment'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']


class Professor(models.Model):
    name = models.CharField('Nombre', max_length=100)
    id_document = models.CharField('Cedula',max_length=20)
    birth_date = models.DateTimeField('F. Nacimiento', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='professors')
    gender = models.CharField('Sexo',max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField('Activo(a) ?',default=True)
    created_at = models.DateTimeField('F. Creacion', auto_now_add=True)
    updated_at = models.DateTimeField('F. Modificacion', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_professors')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_professors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profesor-detail', kwargs={'pk': self.id})
        
    class Meta:
        # db_table = 'professor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['name']
