from django.urls import path

from reviews.api import views

urlpatterns = [
    path('get/', views.ReviewListAPIView.as_view(), name='get_review')
]