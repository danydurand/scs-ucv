from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sce.models import School
from sce.modules.utils import navegation


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'sce/school/school_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['school_keys'] = [item.id for item in context['object_list']]
        return context


class SchoolDetailView(LoginRequiredMixin, DetailView):
    model = School
    template_name = 'sce/school/school_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = context['school'].departments.all()
        keys = []
        if 'school_keys' in self.request.session:
            keys = self.request.session['school_keys']
        prev_item, next_item = navegation(context['school'].id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        return context


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    template_name = 'sce/school/school_form.html'
    fields = ['name', 'faculty']
    success_url = reverse_lazy('school-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = form.instance.name.upper()
        return super().form_valid(form)


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    template_name = 'sce/school/school_form.html'
    fields = ['name', 'faculty']
    redirect = 'school-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.name = form.instance.name.upper()
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


