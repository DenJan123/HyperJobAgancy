from django import forms
from .models import *


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']

