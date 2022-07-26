from django import forms
from sce.models import School
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class SchoolForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={
            'Placeholder': 'Name',
            'style': 'text-transform: capitalize;'
        })
    )

    class Meta:
        model = School
        exclude = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def clean(self):
        data = self.cleaned_data
        name = data['name']
        faculty = data['faculty']
        faculty = self.cleaned_data.get('faculty')
        edit = True if self.instance else False
        if edit:
            if School.objects.filter(name=name, faculty=faculty)\
                .exclude(id=self.instance.id)\
                .exists():
                raise forms.ValidationError(
                    f'This name is already exists asociated to the Faculty !!')
        else:
            if School.objects.filter(name=name, faculty=faculty)\
                .exists():
                raise forms.ValidationError(
                    f'This name is already exists asociated to the Faculty !!')
        return data
