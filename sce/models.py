from django.db import models
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
        
    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.name}</a>'

    @property
    def school_qty(self):
        return self.schools.count()

    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'faculty')"

    class Meta:
        ordering = ['name']


class School(models.Model):
    name = models.CharField(max_length=100)
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
        
    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.name}</a>'

    @property
    def department_qty(self):
        return self.departments.count()

    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'school')"
    
    class Meta:
        ordering = ['name']


class Department(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_departments')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_departments')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.id})
        
    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.name}</a>'

    @property
    def professor_qty(self):
        return self.professors.count()
    
    @property
    def asignature_qty(self):
        return self.asignatures.count()
    
    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'department')"

    class Meta:
        ordering = ['name']


class Professor(models.Model):
    name = models.CharField(max_length=100)
    id_document = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='professors')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_professors')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_professors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('professor-detail', kwargs={'pk': self.id})
        
    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.name}</a>'

    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'professor')"

    class Meta:
        ordering = ['name']


ASIGNATURE_CHOICES = (
    ('M', 'MANDATORY'),
    ('O', 'OPTIONAL'),
)

class Asignature(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    asignature_type = models.CharField(max_length=1, choices=ASIGNATURE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_exempted_interships = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='asignatures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_asignatures')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_asignatures')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asignature-detail', kwargs={'pk': self.id})
        
    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.code}</a>'

    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'asignature')"

    class Meta:
        ordering = ['name']


class Pensum(models.Model):
    name = models.CharField(max_length=7, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_pensums')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_pensums')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pensum-detail', kwargs={'pk': self.id})

    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self.name}</a>'

    @property
    def details_qty(self):
        return self.details.count()

    @property
    def exists_detail_by_semester(self, semester):
        return self.details.objects.filter(semester=semester).exists()

    def get_details_by_semester(self, semester):
        return self.details.objects.filter(semester=semester).all()

    @property
    def delete_record_string(self):
        return f"deleteRecord({self.id}, '{self.name}', 'pensum')"

    class Meta:
        ordering = ['name']


SEMESTER_CHOICES = [
    [None, 'SEMESTER'],
    [1, 'FIRST'],
    [2, 'SECOND'],
    [3, 'THIRD'],
    [4, 'FOURTH'],
    [5, 'FIFTH'],
    [6, 'SIXTH'],
    [7, 'SEVENTH'],
    [8, 'EIGHTH'],
    [9, 'NINETH'],
    [10, 'TENTH'],
]


class PensumDetail(models.Model):
    pensum = models.ForeignKey(Pensum, related_name='details', on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    asignature = models.ForeignKey(Asignature, related_name='pensum_detail', on_delete=models.CASCADE)
    credits = models.IntegerField()
    prelated_by = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.pensum.name, self.semester, self.asignature.name)

    class Meta:
        ordering = ['pensum','semester','id']

    def get_absolute_url(self):
        return reverse('pensum-detail', kwargs={'pk': self.pensum_id})

    def link(self):
        return f'<a href="{self.get_absolute_url()}">{self}</a>'
