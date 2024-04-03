from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import DokumenForm
from .models import DokumenModel

# Create your views here.


@permission_required('dokumen.view_dokumenmodel')
def list_dokumen(request):
  data = DokumenModel.objects.all()
  context  = {
    'data' : data,
    'modul' : 'Dokumen', 
    'links' : {
      'create': 'create-dokumen',
      'delete': 'delete-dokumen',
      'edit': 'edit-dokumen',
    
    }, 
    'parameter': {
      'dokumen' : True,
      'data_master': True
    }
  }

  return render(request, 'list_dokumen.html', context)

@permission_required('dokumen.add_dokumenmodel')
def create_dokumen(request):
  if request.method == 'GET':
    context = {
      'form' : DokumenForm(),
      'modul': 'Dokumen',
      'links': {
        'list': 'list-dokumen'
      }
    }

    return render(request, 'dokumen_form.html', context)
  
  elif request.method  == 'POST':
    form = DokumenForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('list-dokumen')
    
@permission_required('dokumen.change_dokumenmodel')
def edit_dokumen(request, pk):
  dokumen = get_object_or_404(DokumenModel, id=pk)
  context = {
      'form' : DokumenForm(instance=dokumen),
      'id': id,
      'modul': 'Dokumen',
      'links': {
        'list': 'list-dokumen'
      }
    }

  if request.method == 'GET':
    return render(request, 'dokumen_form.html', context)
  
  elif request.method == 'POST':
    form = DokumenForm(request.POST, instance=dokumen)

    if form.is_valid():
      form.save()
      return redirect('list-dokumen')
    
    else:
      return render(request, 'dokumen_form.html',  {'form': form})
      
     
@permission_required('dokumen.delete_dokumenmodel')
def delete_dokumen(request, id):
  dokumen = get_object_or_404(DokumenModel, id=id)
  dokumen.delete()
  return redirect('list-dokumen')
    




