from django.urls import path
# from . import views
from .views.faculty.views import * 
from .views.school.views import * 
from .views.department.views import * 


urlpatterns = [
    path('', index, name='index'),

    path('department_list/', DepartmentListView.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('department/create', DepartmentCreateView.as_view(), name='department-create'),
    path('department/<int:pk>/delete', DepartmentDeleteView.as_view(), name='department-delete'),

    path('school_list/', SchoolListView.as_view(), name='school-list'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('school/<int:pk>/update', SchoolUpdateView.as_view(), name='school-update'),
    path('school/create', SchoolCreateView.as_view(), name='school-create'),
    path('school/<int:pk>/delete', SchoolDeleteView.as_view(), name='school-delete'),

    path('faculty_list/', FacultyListView.as_view(), name='faculty-list'),
    path('faculty/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),
    path('faculty/<int:pk>/update', FacultyUpdateView.as_view(), name='faculty-update'),
    path('faculty/create', FacultyCreateView.as_view(), name='faculty-create'),
    path('faculty/<int:pk>/delete', FacultyDeleteView.as_view(), name='faculty-delete'),
]
