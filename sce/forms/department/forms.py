from django import forms 
from sce.models import Department
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class DepartmentSchoolForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'Placeholder': 'Department Name',
            'style': 'text-transform: capitalize;'
        })
    )
    school = forms.IntegerField()

    class Meta:
        model = Department
        exclude = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def clean_name(self):
        school = self.cleaned_data['school']
        name = self.cleaned_data['name']
        if Department.objects.filter(name=name, school=school)\
            .exists():
            raise forms.ValidationError(
                f'This School-Departemt combination already exists !!')
