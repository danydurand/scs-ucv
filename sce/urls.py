from django.urls import path
# from . import views
from .views.faculty.views import * 
from .views.school.views import * 
from .views.department.views import * 
from .views.professor.views import * 
from .views.asignature.views import * 


urlpatterns = [
    path('', index, name='index'),

    path('asignature_list/', AsignatureListView.as_view(), name='asignature-list'),
    path('asignature/<int:pk>/', AsignatureDetailView.as_view(), name='asignature-detail'),
    path('asignature/<int:pk>/update', AsignatureUpdateView.as_view(), name='asignature-update'),
    path('asignature/create', AsignatureCreateView.as_view(), name='asignature-create'),
    path('asignature/<int:pk>/delete', AsignatureDeleteView.as_view(), name='asignature-delete'),

    path('professor_list/', ProfessorListView.as_view(), name='professor-list'),
    path('professor/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('professor/<int:pk>/update', ProfessorUpdateView.as_view(), name='professor-update'),
    path('professor/create', ProfessorCreateView.as_view(), name='professor-create'),
    path('professor/<int:pk>/delete', professor_delete, name='professor-delete'),
    # path('professor/<int:pk>/delete', ProfessorDeleteView.as_view(), name='professor-delete'),

    path('department_list/', DepartmentListView.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('department/create', DepartmentCreateView.as_view(), name='department-create'),
    path('department/<int:pk>/delete', department_delete, name='department-delete'),
    # path('department/<int:pk>/delete', DepartmentDeleteView.as_view(), name='department-delete'),

    path('school_list/', SchoolListView.as_view(), name='school-list'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('school/<int:pk>/update', SchoolUpdateView.as_view(), name='school-update'),
    path('school/create', SchoolCreateView.as_view(), name='school-create'),
    path('school/<int:pk>/delete', school_delete, name='school-delete'),
    # path('school/<int:pk>/delete', SchoolDeleteView.as_view(), name='school-delete'),

    path('faculty_list/', FacultyListView.as_view(), name='faculty-list'),
    path('faculty/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),
    path('faculty/<int:pk>/update', FacultyUpdateView.as_view(), name='faculty-update'),
    path('faculty/create', FacultyCreateView.as_view(), name='faculty-create'),
    path('faculty/<int:pk>/delete', faculty_delete, name='faculty-delete'),
    # path('faculty/<int:pk>/delete', FacultyDeleteView.as_view(), name='faculty-delete'),
]
