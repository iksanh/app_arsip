from django.urls import path
from wkhtmltopdf.views import PDFTemplateView
from .views import ArsipListView, ArsipCreate, ArsipUpdate, arsip_delete, arsip_report_excel, generate_pdf_report, generate_pdf_report_view


urlpatterns = [
  path('', ArsipListView.as_view(), name='list-arsip'),
  path('create/', ArsipCreate.as_view(), name='create-arsip'),
  path('edit/<str:pk>', ArsipUpdate.as_view(), name='edit-arsip'),
  path('delete/<str:id>', arsip_delete, name='delete-arsip'),
  path('report_excel/', arsip_report_excel, name='arsip-report'),
  
  path('pdf/', generate_pdf_report, name='arsip-report-pdf'),
  path('report_pdf/', generate_pdf_report_view, name='arsip-report-pdf'),
 


]