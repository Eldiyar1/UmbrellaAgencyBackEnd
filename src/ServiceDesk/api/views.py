from rest_framework import generics

from .serializers import ApplicationFormSerializer
from ServiceDesk.models import ApplicationForm


class ApplicationFormCreateAPIView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
