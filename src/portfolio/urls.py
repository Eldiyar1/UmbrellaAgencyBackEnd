from django.urls import path

from portfolio.api import views

urlpatterns = [
    path('get/', views.PortfolioListAPIView.as_view(), name='get_portfolio')
]
