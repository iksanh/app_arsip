from django.urls import path
from .views import rekap_report, detail_report, detail_report_get, print_detail_report


urlpatterns = [
  path('rekap/', rekap_report, name='rekap_report'),
  path('detail/get/', detail_report_get, name='detail_report_get'),
  path('detail/print/', print_detail_report, name='detail_report_print'),
  path('detail/', detail_report, name='detail_report'),
]