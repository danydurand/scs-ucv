from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from sce.models import Pensum, PensumDetail, Asignature, SEMESTER_CHOICES
from sce.modules.utils import navegation
import json


class PensumListView(LoginRequiredMixin, ListView):
    model = Pensum
    template_name = 'sce/pensum/pensum_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['pensum_keys'] = [item.id for item in context['object_list']]
        return context


class PensumDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        object = get_object_or_404(Pensum, id=pk)
        context = {
            'object': object,
            'semesters': SEMESTER_CHOICES,
        }
        keys = []
        if 'pensum_keys' in self.request.session:
            keys = self.request.session['pensum_keys']
        prev_item, next_item = navegation(object.id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        self.request.session['pensum_id'] = object.id
        return render(request, 'sce/pensum/pensum_detail.html', context)

    def post(self, request, pk):
        print('POST:',request.POST)
        pensum = get_object_or_404(Pensum, pk=self.request.session['pensum_id'])
        asignature = Asignature.objects.filter(code=request.POST.get('code')).get()
        semester = request.POST.get('semester')
        prelated_by = request.POST.get('prelated_by')
        credits = request.POST.get('credits')

        print('Datos', pensum, asignature, semester, prelated_by, credits)

        detail = PensumDetail.objects.create(
            pensum=pensum,
            asignature=asignature,
            semester=semester,
            prelated_by=prelated_by,
            credits=credits,
        )
        messages.success(request, f'Detail added')
        context = {
            'object': pensum,
            'semesters': SEMESTER_CHOICES,
        }
        return render(request, 'sce/pensum/pensum_detail.html', context)


# class PensumDetailView(LoginRequiredMixin, DetailView):
#     model = Pensum
#     template_name = 'sce/pensum/pensum_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         keys = []
#         if 'pensum_keys' in self.request.session:
#             keys = self.request.session['pensum_keys']
#         prev_item, next_item = navegation(context['pensum'].id, keys)
#         context['prev_item'] = prev_item
#         context['next_item'] = next_item
#         self.request.session['pensum'] = {'pesum':context['pensum'].id}
#         return context


class PensumCreateView(LoginRequiredMixin, CreateView):
    model = Pensum
    template_name = 'sce/pensum/pensum_form.html'
    fields = ['name']
    success_url = reverse_lazy('pensum-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = form.instance.name.upper()
        messages.success(self.request, 'Pensum Created !!')
        return super().form_valid(form)


class PensumUpdateView(LoginRequiredMixin, UpdateView):
    model = Pensum
    template_name = 'sce/pensum/pensum_form.html'
    fields = ['name']
    redirect = 'pensum-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.name = form.instance.name.upper()
        messages.success(self.request, 'Pensum Updated !!')
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


def pensum_delete(request, pk):
    object = get_object_or_404(Pensum, pk=pk)
    object.delete()
    messages.success(request, 'Pensum Deleted !!')
    return redirect(to='pensum-list')


class PensumDeleteView(LoginRequiredMixin, DeleteView):
    model = Pensum
    template_name = 'sce/pensum/pensum_confirm_delete.html'
    success_url = '/pensum_list/'


@login_required
def add_pensum_detail(request):
    
    print(request.session.POST)

    pensum = get_object_or_404(Pensum, pk=request.session['pensum'])
    asignature = request.POST.get('asignature')
    semester = request.POST.get('semester')
    prelated_by = request.POST.get('prelated_by')
    credits = request.POST.get('credits')

    print('Datos', pensum, asignature, semester, prelated_by, credits)

    detail = PensumDetail.objects.get_or_create(
        pensum=pensum,
        asignature=asignature,
        semester=semester,
        prelated_by=prelated_by,
        credits=credits,
    )
    messages.success(request, f'Detail added')
    return render(request, 'partials/film-list.html', {'object': pensum})
