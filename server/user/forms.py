from django import forms

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission



class UserFormSetting(forms.ModelForm):

  current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
  new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)


  class Meta:
    model = User
    fields = ['username', 'email']


  def clean_current_password(self):
    current_password = self.cleaned_data.get('current_password')
    user = self.instance
    if not user.check_password(current_password):
      raise forms.ValidationError('Password sekarang salah')
    
    return current_password
  
  def clean_new_password(self):
    new_password = self.cleaned_data.get('new_password')

    try:
      #validasi password menggunkana django password validator
      validate_password(new_password, self.instance)
    except DjangoValidationError as e:
      #if password validasi gagal tampilkan error
      raise forms.ValidationError('\n'.join(e.messages))
    
    return new_password
  
  


class RegisterUserForm(UserCreationForm):
    qs_group = Group.objects.all()
    groups = forms.ModelMultipleChoiceField(queryset=qs_group, widget=forms.CheckboxSelectMultiple, required=False)
    email = forms.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        #buat instance
        instance = super().save(commit=commit)
        instance.groups.clear()

        for option_group in self.cleaned_data['groups']:
            instance.groups.add(option_group)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'groups')

class UpdateUserForm(forms.ModelForm):
    qs_group = Group.objects.all()
    groups = forms.ModelMultipleChoiceField(queryset=qs_group, widget=forms.CheckboxSelectMultiple, required=False)
    username = forms.CharField(disabled= True)

    class Meta:
        model = User
        fields = ('username','groups','is_active', 'is_superuser', 'email')












