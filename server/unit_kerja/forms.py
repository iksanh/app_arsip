from django import forms
from .models import UnitKerjaModel, SubUnitKerjaModel

class UnitKerjaForm(forms.ModelForm):
  class Meta:
    model = UnitKerjaModel
    fields = ['name', 'arsip']

    labels = {'arsip': 'Kode Arsip', 'name': 'Nama Unit Kerja'}


class SubUnitKerjaForm(forms.ModelForm):
  class Meta:
    model = SubUnitKerjaModel
    fields =  ['unit_kerja','name']

  def __init__(self, *args, **kwargs):
    super(SubUnitKerjaForm, self).__init__(*args, **kwargs)
    self.fields['unit_kerja'].widget.attrs['class'] = 'form-select'
