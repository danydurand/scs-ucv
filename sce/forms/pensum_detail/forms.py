from django import forms
from sce.models import SEMESTER_CHOICES, Asignature, PensumDetail


class PensumDetailForm(forms.Form):
    asignature = forms.CharField(
        label='',
        max_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Code',
            # 'style': 'width: 80%'
        })
    )
    semester = forms.ChoiceField(
        label='', 
        choices=SEMESTER_CHOICES,
    )
    prelated_by = forms.CharField(
        label='', 
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g: 9908-9611',
            # 'style': 'text-transform: capitalize; width: 80%'
        })
    )
    credits = forms.CharField(
        label='', 
        max_length=1, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Credits',
            # 'style': 'text-transform: capitalize; width: 80%'
        })
    )

    def clean(self):
        from django.core.exceptions import ValidationError
        #------------------------------------------------
        # Asignature must exists
        #------------------------------------------------
        asignature = self.cleaned_data['asignature']
        if not Asignature.objects.filter(code=asignature).exists():
            raise ValidationError(f'Asignature {asignature} does not exist!!')
        #------------------------------------------------
        # Prelated_by asignatures must exist
        #------------------------------------------------
        prelated_by = self.cleaned_data['prelated_by']
        length = len(prelated_by)
        if length:
            if length > 4 and prelated_by.find('-') == -1:
                raise ValidationError(
                    f'Use Prelated asignatures in the correct format, e.g. 9403-9611')
            asignatures = prelated_by.split('-')
            for asignature in asignatures:
                if not Asignature.objects.filter(code=asignature).exists():
                    raise ValidationError(f'Asignature {asignature} does not exist !!')
        #------------------------------------------------
        # Semester-Asignature combination must be unique
        #------------------------------------------------
        semester = self.cleaned_data['semester']
        code = self.cleaned_data['asignature']
        asignature = Asignature.objects.filter(code=code).get()
        if PensumDetail.objects.filter(
            asignature=asignature, semester=semester
            ).exists():
            raise ValidationError(f'Asignature: {code} Semester {semester} combination, already exists !!')
