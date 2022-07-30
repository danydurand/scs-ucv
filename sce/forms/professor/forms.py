from django import forms 
from sce.models import Professor, GENDER_CHOICES
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ProfessorForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'Placeholder': 'Professor Name',
            'style': 'text-transform: capitalize; width: 98%'
        })
    )
    id_document = forms.CharField(
        label='',
        min_length=6,
        max_length=20,
        # required=True,
        widget=forms.TextInput(attrs={
            'Placeholder': 'Id Doc.',
            'style': 'text-transform: capitalize; width: 80%'
        })
    )
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = forms.CharField(
        label="",
        widget=forms.Select(
            choices=GENDER_CHOICES,
            attrs={ 'style': 'width: 100%' })
    )
    is_active = forms.BooleanField()

    class Meta:
        model = Professor
        exclude = ['birth_date', 'created_at', 'created_by', 'updated_at', 'updated_by']

    def clean_id_document(self):
        print('validando el id doc')
        id_document = self.cleaned_data['id_document']
        if Professor.objects.filter(id_document=id_document).exists():
            raise forms.ValidationError(
                f'There is another Professor with this Id Doc !!')
        else:
            print('Todo bien con la validacion!!')
