from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Umbrella API",
        default_version='v1',
        description="API for Umbrella project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="myworkingartur@gmail.com", ),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns_api_v1 = [
    path('portfolio/', include('portfolio.urls'))
]

urlpatterns_swagger = [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_api_v1)),
    path('', include(urlpatterns_swagger))
]
