from django.urls import path

from .api import views

urlpatterns = [
    path('get/', views.FounderListAPIView.as_view(), name='get_founders'),
    path('get/', views.VacancyListAPIView.as_view(), name='get_vacancy')
]
