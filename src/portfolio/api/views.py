from rest_framework import generics

from portfolio import models as port_mod
from portfolio.api import serializers as port_ser


class PortfolioListAPIView(generics.ListAPIView):
    queryset = port_mod.Portfolio.objects.all()
    serializer_class = port_ser.PortfolioSerializer
