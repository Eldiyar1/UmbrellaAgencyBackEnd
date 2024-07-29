from rest_framework import generics

from about import models as about_mod
from about.api import serializers as about_ser


class FounderListAPIView(generics.ListAPIView):
    queryset = about_mod.Founder.objects.all()
    serializer_class = about_ser.FounderSerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = about_mod.Vacancy.objects.all()
    serializer_class = about_ser.VacancySerializer