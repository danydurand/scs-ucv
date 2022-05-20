from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.urls import reverse


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('faculty-detail', kwargs={'pk': self.id})
        
    @property
    def school_qty(self):
        return self.schools.count()
    
    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        ordering = ['name']


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='schools')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school-detail', kwargs={'pk': self.id})
        
    @property
    def department_qty(self):
        return self.departments.count()
    
    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'
        ordering = ['name']


class Department(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.id})
        
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']