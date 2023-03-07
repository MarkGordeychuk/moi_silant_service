from django.urls import path

from .views import MachineListAPIView, MachineRetrieveAPIView, MaintenanceListAPIView, MaintenanceUpdateAPIView,\
    ComplaintListAPIView, ComplaintUpdateAPIView, DirectoryRetrieveAPIView

urlpatterns = [
    path('', MachineListAPIView.as_view()),
    path('machine/<str:pk>/', MachineRetrieveAPIView.as_view()),
    path('maintenance/', MaintenanceListAPIView.as_view()),
    path('maintenance/<int:pk>/', MaintenanceUpdateAPIView.as_view()),
    path('complaint/', ComplaintListAPIView.as_view()),
    path('complaint/<int:pk>/', ComplaintUpdateAPIView.as_view()),
    path('directory/<int:pk>/', DirectoryRetrieveAPIView.as_view()),
]
