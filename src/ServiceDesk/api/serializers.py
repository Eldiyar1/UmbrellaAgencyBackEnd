from rest_framework import serializers

from ServiceDesk.models import ApplicationForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y Время: %H', read_only=True)

    class Meta:
        model = ApplicationForm
        fields = '__all__'



