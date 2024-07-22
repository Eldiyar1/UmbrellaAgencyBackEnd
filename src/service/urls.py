from django.urls import path

from service.api import views

urlpatterns = [
    path('get/', views.ServiceListAPIView.as_view(), name='service_get')
]