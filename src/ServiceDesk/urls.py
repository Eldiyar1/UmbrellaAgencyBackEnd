from django.urls import path

from .api import views

urlpatterns = [
    path('create/', views.ApplicationFormCreateAPIView.as_view(), name='create_form')
]
