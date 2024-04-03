from django import forms
from .models import ArsipModel
from klasifikasi.models import KlasifikasiModel
from pegawai.models import PegawaiModel

from django_select2.forms import Select2Widget
KETERANGAN_CHOICE = [('', 'PILIH KETARANGAN'),('SURAT MASUK', 'SURAT MASUK'), ('SURAT KELUAR', 'SURAT KELUAR'), ('LAINNYA', 'LAINNNYA')]

class ArsipForm(forms.ModelForm):
  
  
  
  class Meta:
    model = ArsipModel
    exclude = ['created_by', 'created_at', 'updated_by','update_at']
    
  


  def __init__(self, user=None, *args, **kwargs):

    
    super(ArsipForm, self).__init__(*args, **kwargs)
    
    
        # Set initial value for tanggal_dokumen field
    self.fields['tanggal_dokumen'].initial = kwargs.get('instance', None).tanggal_dokumen if kwargs.get('instance') else None

    if user and not user.is_superuser:
       pegawai = PegawaiModel.objects.filter(user_profile = user).first()
   
       unit_kerja = pegawai.unit_kerja
    
       self.fields['kode_klasifikasi'].queryset= KlasifikasiModel.objects.filter(kode_klasifikasi__icontains=unit_kerja.arsip)

 
    self.fields['file'].widget.attrs['class'] = 'form-control'
       

    self.fields['uraian'].widget.attrs.update({'style': 'height : 100px'})
    self.fields['tanggal_dokumen'].widget = forms.DateInput(attrs={'type': 'date'})
    self.fields['keterangan'].widget = forms.Select(choices=KETERANGAN_CHOICE)
    
 
    

    fields_to_modify = ['pencipta', 'pengelola', 'keterangan']
    for field_name in fields_to_modify:
            widget_classes = self.fields[field_name].widget.attrs.get('class', '').split()
            if 'form-control' in widget_classes:
                widget_classes.remove('form-control')
                self.fields[field_name].widget.attrs['class'] = ' '.join(widget_classes)
    
    

    #change label 
    self.fields['uraian'].label = 'Uraian / Perihal'
    self.fields['no_arsip'].label = 'Nomor Dokumen'

      