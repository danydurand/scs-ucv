from django import forms
from sce.models import Asignature
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class AsignatureForm(forms.ModelForm):
    code = forms.CharField(
        min_length=4,
        max_length=4,
        validators=[RegexValidator(
            r'^[0-9]*$', message='Only numbers allowed.')],
        widget=forms.TextInput(attrs={
            'Placeholder': 'Code',
            # 'style': 'font-size: 13px'
        })
    )
    name = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'Placeholder': 'Name',
            'style': 'text-transform: capitalize;'
        })
    )

    class Meta:
        model = Asignature
        exclude = ['created_at', 'updated_by', 'updated_at', 'updated_by']

    def clean_code(self):
        code = self.cleaned_data.get('code')
        edit = True if self.instance else False
        if edit:
            if Asignature.objects.filter(code=code).exclude(id=self.instance.id).exists():
                raise forms.ValidationError(f'This code is already exists !!')
        else:
            if Asignature.objects.filter(code=code).exists():
                raise forms.ValidationError(f'This code is already exists !!')
        return code

    def clean_name(self):
        name = self.cleaned_data.get('name')
        edit = True if self.instance else False
        if edit:
            if Asignature.objects.filter(name=name).exclude(id=self.instance.id).exists():
                raise forms.ValidationError(f'This name is already exists !!')
        else:
            if Asignature.objects.filter(name=name).exists():
                raise forms.ValidationError(f'This name is already exists !!')
        return name
