from django.urls import path

from service.api import views

urlpatterns = [
    path('get/', views.ServiceListAPIView.as_view(), name='service_get'),
    path('main_page/', views.ServiceMainPageListAPIView.as_view(), name='service_get_main'),
    ]
