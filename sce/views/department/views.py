from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sce.models import Department


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'sce/department/department_list.html'


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'sce/department/department_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['department_list'] = Department.objects.filter(school=context['school'])
    #     return context

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'sce/department/department_form.html'
    fields = ['name', 'school']
    redirect = 'department-detail'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = 'sce/department/department_form.html'
    fields = ['name', 'school']
    redirect = 'department-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'sce/department/department_confirm_delete.html'
    success_url = '/department_list/'



