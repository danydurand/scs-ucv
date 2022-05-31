from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from sce.models import *
from sce.modules.utils import navegation


@login_required
def index(request):
    school_qty = School.objects.count()
    depart_qty = Department.objects.count()
    context    = {
        'school_qty': school_qty,
        'depart_qty': depart_qty,
    }
    return render(request, 'index.html', context)


class FacultyListView(LoginRequiredMixin, ListView):
    model = Faculty
    template_name = 'sce/faculty/faculty_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['faculty_keys'] = [item.id for item in context['object_list']]
        return context


class FacultyDetailView(LoginRequiredMixin, DetailView):
    model = Faculty
    template_name = 'sce/faculty/faculty_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_list'] = context['faculty'].schools.all()
        keys = []
        if 'faculty_keys' in self.request.session:
            keys = self.request.session['faculty_keys']
        prev_item, next_item = navegation(context['faculty'].id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        return context


class FacultyCreateView(LoginRequiredMixin, CreateView):
    model = Faculty
    template_name = 'sce/faculty/faculty_form.html'
    fields = ['name','is_active']
    success_url = reverse_lazy('faculty-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = form.instance.name.upper()
        return super().form_valid(form)



class FacultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Faculty
    template_name = 'sce/faculty/faculty_form.html'
    fields = ['name','is_active']
    redirect = 'faculty-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.name = form.instance.name.upper()
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class FacultyDeleteView(LoginRequiredMixin, DeleteView):
    model = Faculty
    template_name = 'sce/faculty/faculty_confirm_delete.html'
    success_url = '/faculty_list/'

