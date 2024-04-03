from django import forms
from .models import SirkulasiModel

class SirkluasiForm(forms.ModelForm):
    
    class Meta:
        model = SirkulasiModel
        fields = '__all__'
        exclude = ['created_by', 'created_at', 'updated_by','updated_at']
        

    def __init__(self, *args, **kwargs):
        super(SirkluasiForm, self).__init__(*args, **kwargs)
        self.fields['keperluan'].widget.attrs.update({'style': 'height : 100px'})
        self.fields['tanggal_pinjam'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['tanggal_harus_kembali'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['tanggal_kembali'].widget = forms.DateInput(attrs={'type': 'date'})
        
