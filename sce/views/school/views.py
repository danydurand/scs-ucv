from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sce.models import School, Department


class SchoolListView(ListView):
    model = School
    template_name = 'sce/school/school_list.html'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'sce/school/school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['department_list'] = Department.objects.filter(school=context['school'])
        context['department_list'] = context['school'].departments.all()
        return context

