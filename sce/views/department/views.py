from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from sce.models import Department, Professor, Asignature
from sce.forms.professor.forms import ProfessorForm
from sce.modules.utils import navegation


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'sce/department/department_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['department_keys'] = [item.id for item in context['object_list']]
        return context


class DepartmentDetailView(LoginRequiredMixin, View):
    
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        context = {
            'department': department,
            'professor_list': department.professors.all(),
            'asignature_list': department.asignatures.all(),
        }
        keys = []
        if 'department_keys' in self.request.session:
            keys = self.request.session['department_keys']
        prev_item, next_item = navegation(context['department'].id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        return render(request, 'sce/department/department_detail.html', context)

    def post(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        professor_name = request.POST.get('professor_name')
        if len(professor_name):
            id_document = request.POST.get('id_document')
            gender = request.POST.get('gender')
            #------------------
            # Data validation
            #------------------
            Professor.objects.create(
                name=professor_name,
                department=department,
                id_document=id_document,
                gender=gender,
                created_by=request.user
            )
            messages.success(request, 'Professor Added !!')
        else:
            code = request.POST.get('code')
            if len(code):
                name = request.POST.get('name')
                type_asignature = request.POST.get('type_asignature')
                #------------------
                # Data validation
                #------------------
                Asignature.objects.create(
                    code=code,
                    name=name,
                    type_asignature=type_asignature,
                    created_by=request.user
                )
                messages.success(request, 'Asignature Added !!')

        return redirect(to='department-detail', pk=pk)



# class DepartmentDetailView(LoginRequiredMixin, DetailView):
#     model = Department
#     template_name = 'sce/department/department_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['professor_list'] = context['department'].professors.all()
#         context['asignature_list'] = context['department'].asignatures.all()
#         keys = []
#         if 'department_keys' in self.request.session:
#             keys = self.request.session['department_keys']
#         prev_item, next_item = navegation(context['department'].id, keys)
#         context['prev_item'] = prev_item
#         context['next_item'] = next_item
#         return context


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'sce/department/department_form.html'
    fields = ['name', 'school']
    success_url = reverse_lazy('department-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.name = form.instance.name.title()
        return super().form_valid(form)


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = 'sce/department/department_form.html'
    fields = ['name', 'school']
    redirect = 'department-detail'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.name = form.instance.name.title()
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


def department_delete(request, pk):
    object = get_object_or_404(Department, pk=pk)
    object.delete()
    messages.success(request, 'Department Deleted !!')
    return redirect(to='department-list')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'sce/department/department_confirm_delete.html'
    success_url = '/department_list/'



