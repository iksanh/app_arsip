from django import forms
from .models import DokumenModel


class DokumenForm(forms.ModelForm):
  class Meta:
    model = DokumenModel
    fields = '__all__'