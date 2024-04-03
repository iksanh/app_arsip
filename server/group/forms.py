from django import forms
from django.contrib.auth.models import Group, Permission


class GroupForm(forms.ModelForm):
  permissions = Permission
  class Meta: 
    model = Group
    fields  = ['name', 'permissions']

  
  permissions = forms.ModelMultipleChoiceField(
    widget = forms.CheckboxSelectMultiple,
    queryset=Permission.objects.all(),
    required=False
  )

  def save(self, commit=True):
    #simpan model ke object 
    instance = super().save(commit=commit)
    instance.permissions.clear()

    for option in self.cleaned_data['permissions']:
      instance.permissions.add(option)

    return instance