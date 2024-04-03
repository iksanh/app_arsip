import functools
from typing import Any
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, FileResponse
from django.utils import timezone
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.template.loader import render_to_string
from openpyxl import Workbook
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,  Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from django.views.generic import DetailView

from .models import ArsipModel
from .forms import ArsipForm
from klasifikasi.models import KlasifikasiModel
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
arsipParams = CrudParams('arsip')

#LIST VIEW 
class ArsipListView(PermissionRequiredMixin, ListView, FormView):
  permission_required = 'arsip.view_arsipmodel' 
  
  model = ArsipModel
  template_name = 'list_arsip.html'
  context_object_name = 'data'
  klasifikasi = KlasifikasiModel.objects.all()

  extra_context = arsipParams.parameter(arsip=True, list_klasifikasi=klasifikasi)

  def get_initial(self):
    initial = super().get_initial()

    #populate initial data from  request .get 
    initial['kode_klasifikasi'] = self.request.GET.get('kode_klasifikasi', '')
    initial['no_arsip'] = self.request.GET.get('no_arsip', '')
    initial['pencipta'] = self.request.GET.get('pencipta', '')
    initial['pengelola'] = self.request.GET.get('pengelola', '')
    initial['tempat'] = self.request.GET.get('tempat', '')
    initial['lokasi'] = self.request.GET.get('lokasi', '')
    initial['keterangan'] = self.request.GET.get('keterangan', '')
    initial['tanggal_dokumen'] = self.request.GET.get('tanggal_dokumen', '')
    initial['jenis_dokumen'] = self.request.GET.get('jenis_dokumen', '')

    return initial
    
    # return super().get_initial()

  def get_form_class(self) -> type:
    return ArsipForm
  
  
  def get_queryset(self) -> QuerySet[Any]:
    query_set = ArsipModel.objects.all()

    #handle search paramater
    search_klasifikasi = self.request.GET.get('kode_klasifikasi', '')
    search_no_arsip = self.request.GET.get('no_arsip', '')
    search_pencipta = self.request.GET.get('pencipta', '')
    search_pengelola = self.request.GET.get('pengelola', '')
    search_tempat = self.request.GET.get('tempat', '')
    search_lokasi = self.request.GET.get('lokasi', '')
    search_keterangan = self.request.GET.get('keterangan', '')
    search_tanggal_dokumen = self.request.GET.get('tanggal_dokumen', '')
    search_jenis_dokumen = self.request.GET.get('jenis_dokumen', '')

    #handle donwnload report 

    action = self.request.GET.get('action', '')


    # Create a Q object to combine filters with the AND operator
    q_object = Q()

    # apply filter 

    if search_jenis_dokumen:
      q_object &= Q(jenis_dokumen=search_jenis_dokumen)

    if search_klasifikasi: 
      q_object &= Q(kode_klasifikasi=search_klasifikasi)
    
    if search_pencipta:
      q_object &= Q(pencipta=search_pencipta)


    if search_no_arsip:
      q_object &= Q(no_arsip__icontains=search_no_arsip)

    if search_pengelola: 
      q_object  &= Q(pengelola=search_pengelola)
    
    if search_lokasi:
      q_object &= Q(lokasi=search_lokasi)

    if search_tempat:
      q_object &= Q(tempat=search_tempat)
      
    if search_keterangan:
      q_object &= Q(keterangan=search_keterangan)
    

    if search_tanggal_dokumen:
      # print(ArsipModel.objects.filter(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d")))
      q_object &= Q(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d"))

    query_set = query_set.filter(q_object)
    # print(query_set)
    print(action)
    if action == 'excel' : 
      print('action == excel')
      arsip_report_excel(self.request, query_set)
    else:  
      return query_set
  
# class ArsipListSearch(PermissionRequiredMixin):



class ArsipCreate(PermissionRequiredMixin, CreateView):
  permission_required =  'arsip.add_arsipmodel'
  form_class = ArsipForm
  template_name =  'create_arsip.html'
  extra_context = arsipParams.parameter(arsip=True, action='Buat Data')
  success_url = reverse_lazy('list-arsip')

 

  def form_valid(self, form: BaseModelForm) -> HttpResponse:
    form.instance.created_at = timezone.now()
    form.instance.update_at = timezone.now()
    form.instance.created_by = self.request.user
    form.instance.updated_by = self.request.user

    return super().form_valid(form)
  
  def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    print(self.request.user)
    return super().get(request, *args, **kwargs)

  def get_form_kwargs(self) -> dict[str, Any]:

    kwargs = super(ArsipCreate, self).get_form_kwargs()
    kwargs['user'] =  self.request.user 
    return kwargs

class ArsipUpdate(PermissionRequiredMixin,UpdateView):
  permission_required = 'arsip.change_arsipmodel'
  model = ArsipModel
  form_class = ArsipForm
  template_name =  'create_arsip.html'
  extra_context = arsipParams.parameter(arsip=True, action='Update Data')
  success_url = reverse_lazy('list-arsip')


  def get_queryset(self) -> QuerySet[Any]:
    return super().get_queryset()
  
  def get_form_kwargs(self) -> dict[str, Any]:
    kwargs = super().get_form_kwargs()

    # set initial value  

    kwargs['initial']['tanggal_dokumen'] = self.object.tanggal_dokumen

    return kwargs

  def form_valid(self, form: BaseModelForm) -> HttpResponse:

    instance = form.save(commit=False)
    new_file = form.cleaned_data['file']
    old_instance = ArsipModel.objects.get(pk=instance.pk)
    if new_file:
      old_file = old_instance.file
      if old_file:
        old_file.delete(save=False)
      instance.file = new_file

    instance.save()
    return super().form_valid(form)


@permission_required('arsip.delete_arsipmodel')
def arsip_delete(req, id):
  arsip = get_object_or_404(ArsipModel, id=id)
  #delete file arsip  = 
  file_to_delete = arsip.file
  if file_to_delete:
    file_to_delete.delete(save=False)
  arsip.delete()
  return redirect('list-arsip')



def arsip_report_excel(request):
  data = ArsipModel.objects.all()
  
  #handle search paramater
  search_klasifikasi = request.GET.get('kode_klasifikasi', '')
  search_no_arsip = request.GET.get('no_arsip', '')
  search_pencipta = request.GET.get('pencipta', '')
  search_pengelola = request.GET.get('pengelola', '')
  search_tempat = request.GET.get('tempat', '')
  search_lokasi = request.GET.get('lokasi', '')
  search_keterangan = request.GET.get('keterangan', '')
  search_tanggal_dokumen = request.GET.get('tanggal_dokumen', '')
  search_jenis_dokumen = request.GET.get('jenis_dokumen', '') 

    # Create a Q object to combine filters with the AND operator
  q_object = Q()

    # apply filter 

  if search_jenis_dokumen:
    q_object &= Q(jenis_dokumen=search_jenis_dokumen)

  if search_klasifikasi: 
    q_object &= Q(kode_klasifikasi=search_klasifikasi)
    
  if search_pencipta:
    q_object &= Q(pencipta=search_pencipta)


  if search_no_arsip:
    q_object &= Q(no_arsip__icontains=search_no_arsip)

  if search_pengelola: 
    q_object  &= Q(pengelola=search_pengelola)
    
  if search_lokasi:
    q_object &= Q(lokasi=search_lokasi)

  if search_tempat:
    q_object &= Q(tempat=search_tempat)
      
  if search_keterangan:
    q_object &= Q(keterangan=search_keterangan)
   

  if search_tanggal_dokumen:
      # print(ArsipModel.objects.filter(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d")))
    q_object &= Q(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d"))

  data = data.filter(q_object)

  # Create a new workbook 
  wb = Workbook()
  ws = wb.active

  #add header 

  ws.append(["Column1", "column 2 ", "column 3"])

      #add data to sheet 

  for item in data:
    ws.append([item.no_arsip, item.pencipta.name, item.pengelola.name])
      #save  the workbook 
        
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = 'attachment; filename=report.xlsx'

  wb.save(response)
  return(response)

def generate_pdf_report(request):
    # Fetch data from ArsipModel
    arsip_data = ArsipModel.objects.all()
      #handle search paramater
    search_klasifikasi = request.GET.get('kode_klasifikasi', '')
    search_no_arsip = request.GET.get('no_arsip', '')
    search_pencipta = request.GET.get('pencipta', '')
    search_pengelola = request.GET.get('pengelola', '')
    search_tempat = request.GET.get('tempat', '')
    search_lokasi = request.GET.get('lokasi', '')
    search_keterangan = request.GET.get('keterangan', '')
    search_tanggal_dokumen = request.GET.get('tanggal_dokumen', '')
    search_jenis_dokumen = request.GET.get('jenis_dokumen', '') 

    # Create a Q object to combine filters with the AND operator
    q_object = Q()

    # apply filter 

    if search_jenis_dokumen:
      q_object &= Q(jenis_dokumen=search_jenis_dokumen)

    if search_klasifikasi: 
      q_object &= Q(kode_klasifikasi=search_klasifikasi)
      
    if search_pencipta:
      q_object &= Q(pencipta=search_pencipta)


    if search_no_arsip:
      q_object &= Q(no_arsip__icontains=search_no_arsip)

    if search_pengelola: 
      q_object  &= Q(pengelola=search_pengelola)
      
    if search_lokasi:
      q_object &= Q(lokasi=search_lokasi)

    if search_tempat:
      q_object &= Q(tempat=search_tempat)
        
    if search_keterangan:
      q_object &= Q(keterangan=search_keterangan)
    

    if search_tanggal_dokumen:
        # print(ArsipModel.objects.filter(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d")))
      q_object &= Q(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d"))

    arsip_data = arsip_data.filter(q_object)
    print(arsip_data)
    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="arsip_report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Define table data
    data = [
        ['No Arsip', 'Jenis Dokumen', 'Pencipta', 'Kode Klasifikasi', 'Tanggal Dokumen', 'Uraian'],
    ]
    for arsip in arsip_data:
        data.append([
            arsip.no_arsip,
            arsip.jenis_dokumen,
            arsip.pencipta,
            arsip.kode_klasifikasi,
            arsip.tanggal_dokumen,
            arsip.uraian
        ])

    # Create table
    table = Table(data)

    # Add style to table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    elements.append(table)

    # Build PDF
    doc.build(elements)
    return response




def generate_pdf_report_view(request):
     # Fetch data from ArsipModel
    arsip_data = ArsipModel.objects.all()

    search_klasifikasi = request.GET.get('kode_klasifikasi', '')
    search_no_arsip = request.GET.get('no_arsip', '')
    search_pencipta = request.GET.get('pencipta', '')
    search_pengelola = request.GET.get('pengelola', '')
    search_tempat = request.GET.get('tempat', '')
    search_lokasi = request.GET.get('lokasi', '')
    search_keterangan = request.GET.get('keterangan', '')
    search_tanggal_dokumen = request.GET.get('tanggal_dokumen', '')
    search_jenis_dokumen = request.GET.get('jenis_dokumen', '') 

    # Create a Q object to combine filters with the AND operator
    q_object = Q()

    # apply filter 

    if search_jenis_dokumen:
      q_object &= Q(jenis_dokumen=search_jenis_dokumen)

    if search_klasifikasi: 
      q_object &= Q(kode_klasifikasi=search_klasifikasi)
      
    if search_pencipta:
      q_object &= Q(pencipta=search_pencipta)


    if search_no_arsip:
      q_object &= Q(no_arsip__icontains=search_no_arsip)

    if search_pengelola: 
      q_object  &= Q(pengelola=search_pengelola)
      
    if search_lokasi:
      q_object &= Q(lokasi=search_lokasi)

    if search_tempat:
      q_object &= Q(tempat=search_tempat)
        
    if search_keterangan:
      q_object &= Q(keterangan=search_keterangan)
    

    if search_tanggal_dokumen:
        # print(ArsipModel.objects.filter(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d")))
      q_object &= Q(tanggal_dokumen=datetime.strptime(search_tanggal_dokumen, "%Y-%m-%d"))

    arsip_data = arsip_data.filter(q_object)

    # Create a buffer to store PDF content
    buffer = BytesIO()

    # Create a PDF document with landscape orientation
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []

    # Define table data
    data = [
        ['No Arsip', 'Jenis Dokumen', 'Pencipta', 'Kode Klasifikasi', 'Tanggal Dokumen', 'Uraian'],
    ]
    for arsip in arsip_data:
        data.append([
            Paragraph(str(arsip.no_arsip), getSampleStyleSheet()['BodyText']),
            Paragraph(str(arsip.jenis_dokumen), getSampleStyleSheet()['BodyText']),
            Paragraph(str(arsip.pencipta), getSampleStyleSheet()['BodyText']),
            Paragraph(str(arsip.kode_klasifikasi), getSampleStyleSheet()['BodyText']),
            str(arsip.tanggal_dokumen),
            Paragraph(arsip.uraian, getSampleStyleSheet()['BodyText'])
        ])

    # Calculate the width of each column
    col_widths = [doc.width / len(data[0]) for _ in data[0]]

    # Create table
    table = Table(data, colWidths=col_widths)

    # Add style to table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    elements.append(table)


     # Add header to each page
    def add_header(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Bold', 12)
        canvas.drawCentredString(doc.pagesize[0] / 2, doc.pagesize[1] - 20, 'Laporan Arsip KANTOR WILAYAH BADAN PERTANAHAN NASIONAL PROVINSI GORONTALO')
        canvas.restoreState()

    #add footer 
     # Add footer to each page
    def add_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        footer_text = f'Gorontalo, {datetime.now().strftime("%d %B %Y")}\nPengelola Arsip\n\nNama Pengelola'
        canvas.drawRightString(doc.pagesize[0] - 10, 10, footer_text)
        canvas.restoreState()


    # Build PDF
    doc.build(elements,onFirstPage=add_header, onLaterPages=add_footer)

    # Get PDF content from buffer
    pdf_content = buffer.getvalue()
    buffer.close()

    # Create HTTP response with PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    return response