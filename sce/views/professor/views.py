from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sce.models import Professor


class ProfessorListView(LoginRequiredMixin, ListView):
    model = Professor
    template_name = 'sce/professor/professor_list.html'


class ProfessorDetailView(LoginRequiredMixin, DetailView):
    model = Professor
    template_name = 'sce/professor/professor_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['professor_list'] = Professor.objects.filter(school=context['school'])
    #     return context

class ProfessorCreateView(LoginRequiredMixin, CreateView):
    model = Professor
    template_name = 'sce/professor/professor_form.html'
    fields = ['name', 'school']
    redirect = 'professor-detail'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class ProfessorUpdateView(LoginRequiredMixin, UpdateView):
    model = Professor
    template_name = 'sce/professor/professor_form.html'
    fields = ['name', 'school']
    redirect = 'professor-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class ProfessorDeleteView(LoginRequiredMixin, DeleteView):
    model = Professor
    template_name = 'sce/professor/professor_confirm_delete.html'
    success_url = '/professor_list/'



