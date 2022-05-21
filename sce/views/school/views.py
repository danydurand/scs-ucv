from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sce.models import School


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'sce/school/school_list.html'


class SchoolDetailView(LoginRequiredMixin, DetailView):
    model = School
    template_name = 'sce/school/school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['department_list'] = Department.objects.filter(school=context['school'])
        context['department_list'] = context['school'].departments.all()
        return context


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    template_name = 'sce/school/school_form.html'
    fields = ['name', 'faculty']
    redirect = 'school-detail'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    template_name = 'sce/school/school_form.html'
    fields = ['name', 'faculty']
    redirect = 'school-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    template_name = 'sce/school/school_confirm_delete.html'
    success_url = '/school_list/'


