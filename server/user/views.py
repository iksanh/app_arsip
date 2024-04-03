from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from django.contrib import messages
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from pegawai.models import PegawaiModel 
from .forms import UserFormSetting, UpdateUserForm, RegisterUserForm
from utils.crud_params import CrudParams
from utils.group import add_user_group


# Create your views here.


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
    # template_name = 'login.html'

    def get_success_url(self):
        #get param next in url
        next_url= self.request.GET.get('next')
        return next_url if next_url else reverse_lazy('home')


    def form_invalid(self, form):
        messages.error(self.request, "Username atau Password salah")
        return self.render_to_response(self.get_context_data(form=form))
    
    
    def form_valid(self, form):
        # Check the POST request fields
        #username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')
        #print(username, password)

        # Do something with the form data

        return super().form_valid(form)




#create paramaters 
userParams = CrudParams('user')

#LIST VIEW 
class UserListView(PermissionRequiredMixin, ListView):
  permission_required = 'user.view_user'
  model = PegawaiModel
  template_name = 'user/list_user.html'
  extra_context = userParams.parameter(data_pegawai=True, user=True)

  

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     
     context = super().get_context_data(**kwargs)
     
     context["data"] = PegawaiModel.objects.exclude(user_profile__isnull=True)
     return context
           

class UserCreate(PermissionRequiredMixin, CreateView):
  permission_required =  'user.add_user'
  model = User
  template_name =  'user/create_user.html'
  fields = '__all__'
  extra_context = userParams.parameter(data_pegawai=True, user=True, action='Buat Data')
  success_url = reverse_lazy('list-unit-kerja')

#Update user For Admin
class UserUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'user.change_user'
  model = User
  form_class = UpdateUserForm
  template_name =  'user/create_user.html'
#   fields = '__all__'
  extra_context = userParams.parameter(data_pegawai=True, user=True, action='Update Data')
  success_url = reverse_lazy('list-user')

@permission_required('user.delete_user')
def user_delete(req, id):
  user = get_object_or_404(User, id=id)
  user.delete()
  return redirect('list-user')

@permission_required('user.add_user')
def create_pegawai_user(request, id):
    pegawai = PegawaiModel.objects.get(id=id)
    user = User.objects.create_user(username=pegawai.identitas, password=pegawai.identitas)
    user.save()

    pegawai.user_profile = user
    pegawai.save()
    # Member(user=user, instance=member).save()
    # print(member.identitas)

    #add user to group
    add_user_group('pengelola', user)

    #set message 
    messages.success(request, f" Pembuatan User {pegawai.nama} berhasil ")
    return redirect('list-pegawai')

def reset_pegawai_password(request, id):
   pegawai = get_object_or_404(PegawaiModel, id=id)
   user = User.objects.get(username=pegawai.identitas)

   
   user.set_password(pegawai.identitas)
   user.save()
   messages.success(request, f"Password Pegawai {pegawai.nama} berahasil di reset " )
   return redirect('list-user')
   


#Update User By User Login 
class UserSettingView(LoginRequiredMixin, UpdateView):
   model = User
   form_class = UserFormSetting
   template_name = 'user/settings.html'
   extra_context = userParams.parameter(data_pegawai=True, user=True, action='Update Data')
   success_url = reverse_lazy('home')


   def get_object(self, querset=None):
      return self.request.user 
   

   def form_valid(self, form):
      
      if form.cleaned_data.get('new_password'):
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['new_password'])
         user.save()
         update_session_auth_hash(self.request, user)

         messages.success(self.request, 'Password Berhasil di Update')

         return super().form_valid(form)
      
      return super().form_valid(form)



class MyUserUpdateView(UpdateView):
    model = User
    # form_class = RegisterUserForm

    template_name = 'user/registration.html'
    extra_context = userParams.parameter(data_pegawai=True, user=True, action='Update Data')

    def get_form_class(self):
        return UpdateUserForm
    def get_success_url(self):
        return reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['groups'] = self.object.groups.all()
        return context

    def form_valid(self, form):
        return super(MyUserUpdateView, self).form_valid(form)

class MyUserUpdateGroup(MyUserUpdateView):
    def get_form_class(self):
        return UpdateUserGroupForm


