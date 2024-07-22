from rest_framework import generics

from service.api import serializers as service_serializer
from service import models as service_mod


class ServiceListAPIView(generics.ListAPIView):
    queryset = service_mod.Service.objects.all()
    serializer_class = service_serializer.ServiceSerializer


