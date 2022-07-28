from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from sce.models import School, Department
from sce.forms.school.forms import SchoolForm
from sce.forms.department.forms import DepartmentSchoolForm
from sce.modules.utils import navegation


class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'sce/school/school_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['school_keys'] = [item.id for item in context['object_list']]
        return context


class SchoolDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        context = { 
            'school': school ,
        }
        keys = []
        if 'school_keys' in self.request.session:
            keys = self.request.session['school_keys']
        prev_item, next_item = navegation(context['school'].id, keys)
        context['prev_item'] = prev_item
        context['next_item'] = next_item
        return render(request, 'sce/school/school_detail.html', context)


    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        name = request.POST.get('name').title()
        feedback = {}
        #---------------------------
        # Name repeated validation
        #---------------------------
        if Department.objects.filter(name=name, school=school).exists():
            feedback['errors'] = ['Department-School combination already exists']
        else:
            Department.objects.create(
                name=name, 
                school=school,
                created_by=request.user
            )
            messages.success(request,'Department added !!')
        context = {
            'school': school,
            'feedback': feedback
        }
        return render(request, 'sce/school/school_detail.html', context)





class SchoolCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = SchoolForm()
        context = {'form': form}
        return render(request, 'sce/school/school_form.html', context)

    def post(self, request):
        form = SchoolForm(request.POST or None)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            messages.success(request, 'School Created !!')
            return redirect(to='school-list')
        else:
            context = {'form': form}
        return render(request, 'sce/school/school_form.html', context)

# class SchoolCreateView(LoginRequiredMixin, CreateView):
#     model = School
#     template_name = 'sce/school/school_form.html'
#     fields = ['name', 'faculty']
#     success_url = reverse_lazy('school-list')

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         form.instance.name = form.instance.name.title()
#         messages.success(self.request, 'School Created !!')
#         return super().form_valid(form)


class SchoolUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        form = SchoolForm(instance=school)
        context = {'form': form}
        return render(request, 'sce/school/school_form.html', context)

    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.instance.updated_by = request.user
            form.save()
            messages.success(request, 'School Updated !!')
            return redirect(to='school-list')
        else:
            context = {'form': form}
        return render(request, 'sce/school/school_form.html', context)


# class SchoolUpdateView(LoginRequiredMixin, UpdateView):
#     model = School
#     template_name = 'sce/school/school_form.html'
#     fields = ['name', 'faculty']
#     redirect = 'school-detail'

#     def form_valid(self, form):
#         form.instance.updated_by = self.request.user
#         form.instance.name = form.instance.name.title()
#         messages.success(self.request, 'School Updated !!')
#         return super().form_valid(form)


def school_delete(request, pk):
    object = get_object_or_404(School, pk=pk)
    object.delete()
    messages.success(request, 'School Deleted !!')
    return redirect(to='school-list')


class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    template_name = 'sce/school/school_confirm_delete.html'
    # messages.success(self.request, 'School Deleted !!')
    success_url = '/school_list/'


def school_more_info(request, pk):
    print('pk',pk)
    obj_school = School.objects.get(pk=pk)
    return render(request, 'sce/school/partials/more_info.html',{'obj_school': obj_school})

def hola(request):
    return HttpResponse('Hola')