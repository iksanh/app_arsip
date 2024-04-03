from django.urls import path
from .views import (UnitKerjaApiList, UnitKerjaApiDetail, SubUnitKerjaApiList,  SubUnitKerjaApiDetail)


urlpatterns =[
    path('', UnitKerjaApiList.as_view()),
    path('<str:pk>', UnitKerjaApiDetail.as_view()),
    path('sub/', SubUnitKerjaApiList.as_view()),
    path('sub/<str:pk>/', SubUnitKerjaApiDetail.as_view())
]




