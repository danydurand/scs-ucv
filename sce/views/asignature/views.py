from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sce.models import Asignature
from sce.modules.utils import navegation


class AsignatureListView(LoginRequiredMixin, ListView):
    model = Asignature
    template_name = 'sce/asignature/asignature_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['asignature_keys'] = [item.id for item in context['object_list']]
        return context


class AsignatureDetailView(LoginRequiredMixin, DetailView):
    model = Asignature
    template_name = 'sce/asignature/asignature_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keys = []
        if 'asignature_keys' in self.request.session:
            keys = self.request.session['asignature_keys']
        prev_item, next_item = navegation(context['asignature'].id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        return context


class AsignatureCreateView(LoginRequiredMixin, CreateView):
    model = Asignature
    template_name = 'sce/asignature/asignature_form.html'
    fields = ['code', 'name', 'asignature_type', 'is_active', 'is_exempted_interships', 'department']
    success_url = reverse_lazy('asignature-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = form.instance.name.upper()
        return super().form_valid(form)



class AsignatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Asignature
    template_name = 'sce/asignature/asignature_form.html'
    fields = ['code', 'name', 'asignature_type', 'is_active', 'is_exempted_interships', 'department']
    redirect = 'asignature-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.name = form.instance.name.upper()
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


def asignature_delete(request, pk):
    object = get_object_or_404(Asignature, pk=pk)
    object.delete()
    messages.success(request, 'Asignature Deleted !!')
    return redirect(to='asignature-list')


class AsignatureDeleteView(LoginRequiredMixin, DeleteView):
    model = Asignature
    template_name = 'sce/asignature/asignature_confirm_delete.html'
    success_url = '/asignature_list/'



