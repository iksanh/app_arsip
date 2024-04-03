"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render

#for upload file
from django.conf import settings
from django.conf.urls.static import static

#view from Tempat
# from lokasi.api.views import TempatListApi, TempatDetailApi

#for securiti
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from user.views import MyLoginView,  logout_then_login

from utils.view import view_pdf


@login_required
def home(req):
    context  = {
        'home' : True,
        'app_name' : 'Aplikasi Pendataan dan Pencarian Arsip Digital Kantor Wilayah BPN Provinsi Gorontalo'
    }
    return render(req, 'dashboard.html', context)
    


urlpatterns = [
    path('', home, name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('admin/', admin.site.urls),

    #FOR REST FRAMEWORK API
    path('api-auth/', include('rest_framework.urls')),
    path('api/user', include('user.api.url')),
    path('api/media/', include('media.api.url')),
    path('api/lokasi/', include('lokasi.api.url')),
    path('api/pegawai/', include('pegawai.api.url')),

    path('api/unitkerja/', include('unit_kerja.api.url')),
    path('api/klasifikasi/', include('klasifikasi.api.url')),
    path('api/arsip/', include('arsip.api.url')),

    #FOR MONOLITH URL

    path('master/unitkerja/', include('unit_kerja.url')),
    path('master/subunitkerja/', include('unit_kerja.url-subunit')),
    path('master/lokasi/', include('lokasi.url')),
    path('master/tempat/', include('lokasi.url_tempat')),
    path('master/media/', include('media.url')),
    path('master/klasifikasi/', include('klasifikasi.url')),
    path('master/pegawai/', include('pegawai.url')),
    path('master/status_pegawai/', include('pegawai.url_status_pegawai')),
    path('master/arsip/', include('arsip.url')),
    path('master/sirkulasi/', include('sirkulasi.url')),
    path('master/user/', include('user.url')),
    path('master/group/', include('group.url')),
    path('master/dokumen/', include('dokumen.url')),
    path('master/pangkat_golongan/', include('pangkat_golongan.url')),
    path('view_pdf/', view_pdf, name='pdf_view'),

    #security
    path('logout/', LogoutView.as_view(), name='logout')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
