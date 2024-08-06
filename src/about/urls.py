from django.urls import path

from .api import views

urlpatterns = [
    path('get_founders/', views.FounderListAPIView.as_view(), name='get_founders'),
    path('get_vacancy/', views.VacancyListAPIView.as_view(), name='get_vacancy')
]
