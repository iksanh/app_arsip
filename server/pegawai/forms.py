from django import forms
from .models import PegawaiModel, PegawaiStatusModel

class PegawaiForm(forms.ModelForm):
  class Meta: 
    model = PegawaiModel
    exclude = ['created_at', 'user_profile']

    labels = {'identitas': 'NIK / NIP', 'status': 'Status Kepegawaian'}
    

class PegawaiStatusForm(forms.ModelForm):
  class Meta:
    model = PegawaiStatusModel
    exclude = ['created_at', 'created_by']

  

    

