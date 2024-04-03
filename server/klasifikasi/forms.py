from django import forms
from .models import KlasifikasiModel

class KlasifikasiForm(forms.ModelForm):
  class Meta:
    model = KlasifikasiModel
    exclude = ['created_at', 'created_by']


  def __init__(self, *args, **kwargs):
    super(KlasifikasiForm, self).__init__(*args, **kwargs)
    self.fields['kategory_arsip'].widget.attrs['class'] = 'form-select'
    self.fields['nasib_akhir'].widget.attrs['class'] = 'form-select'
    self.fields['keterangan'].widget.attrs.update({'style': 'height : 100px'})


