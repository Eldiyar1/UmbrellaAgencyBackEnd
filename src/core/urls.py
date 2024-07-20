from django.contrib import admin
from django.urls import path, include

from core.swagger import urlpatterns_swagger

urlpatterns_api_v1 = [
    path('portfolio/', include('portfolio.urls')),
    path('reviews/', include('reviews.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api_v1)),
    path('', include(urlpatterns_swagger))
]
