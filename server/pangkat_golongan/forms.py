from django import forms
from .models import PangkatGolonganModel

class PangkatGolnganForms(forms.ModelForm):
  class Meta:
    model = PangkatGolonganModel
    fields = '__all__'