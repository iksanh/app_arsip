from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden

class SuperUserRequiredMixin:
  @method_decorator(login_required)

  def dispatch(self, req, *args, **kwargs):
    if not req.user.is_superuser:
      return HttpResponseForbidden("Anda tidak punya akses ke halaman ini")
    
    return super().dispatch(req, *args, **kwargs)
  

def superuser_required(view_func):
  decorated_view_func = method_decorator(login_required)(view_func)

  def wrapper(req, *args, **kwargs):
    if not req.user.is_superuser:
      return HttpResponseForbidden("Anda tidak punya akses ke halaman ini")
    
    return decorated_view_func(req, *args, **kwargs)
  
  return wrapper


