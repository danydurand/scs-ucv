from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sce.models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = 'sce/department/department_list.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'sce/department/department_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['school_list'] = School.objects.filter(faculty=context['faculty'])
    #     return context


