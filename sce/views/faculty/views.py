from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from sce.models import *


def index(request):
    school_qty = School.objects.count()
    depart_qty = Department.objects.count()
    context    = {
        'school_qty': school_qty,
        'depart_qty': depart_qty,
    }
    return render(request, 'index.html', context)


class FacultyListView(ListView):
    model = Faculty
    template_name = 'sce/faculty/faculty_list.html'


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'sce/faculty/faculty_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_list'] = context['faculty'].schools.all()
        return context


class FacultyCreateView(CreateView):
    model = Faculty
    template_name = 'sce/faculty/faculty_form.html'
    fields = ['name']
    redirect = 'faculty-detail'


class FacultyUpdateView(UpdateView):
    model = Faculty
    template_name = 'sce/faculty/faculty_form.html'
    fields = ['name']
    redirect = 'faculty-detail'

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'sce/faculty/faculty_confirm_delete.html'
    success_url = '/faculty_list/'

