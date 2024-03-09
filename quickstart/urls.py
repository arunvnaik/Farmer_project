from django.urls import path
from quickstart.views import FarmerAPIView, CropAPIView, EarningsAPIView,FarmerDetailView,CropDetailView,EarningDetailView

urlpatterns = [
    path('farmers/', FarmerAPIView.as_view(), name='farmers'),
    path('farmers/<int:pk>/', FarmerDetailView.as_view(),name= "farmerdetail"),
    path('crops/', CropAPIView.as_view(), name='crops'),
    path('crops/<int:pk>/',CropDetailView.as_view(),name='cropdetail'),
     path('earnings/', EarningsAPIView.as_view(), name='earnings'),
    path('earnings/<int:pk>/', EarningDetailView.as_view(), name='earningdetail'),
    
]
