from django.contrib import admin
from django.urls import path, include

from core.swagger import urlpatterns_swagger

urlpatterns_api_v1 = [
    path('portfolio/', include('portfolio.urls')),
    path('reviews/', include('reviews.urls')),
    path('service/', include('service.urls')),
    path('form/', include('ServiceDesk.urls')),
    path('about_page/', include('about.urls'))

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api_v1)),
    path('', include(urlpatterns_swagger))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)