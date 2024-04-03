from django import forms
from .models import TempatModel


class TempatForm(forms.ModelForm):
  class Meta:
    model = TempatModel
    fields = '__all__'


  def __init__(self, *args, **kwargs):
    super(TempatForm, self).__init__(*args, **kwargs)

    self.fields['lokasi'].widget.attrs['class'] = 'form-select'
    