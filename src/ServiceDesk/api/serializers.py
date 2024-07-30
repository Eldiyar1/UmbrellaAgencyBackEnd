from rest_framework import serializers
from ServiceDesk.models import ApplicationForm, Service

class ApplicationFormSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y Время: %H', read_only=True)
    service_titles = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )
    services = serializers.StringRelatedField(source='service', many=True, read_only=True)

    class Meta:
        model = ApplicationForm
        fields = (
            'name',
            'number_or_email',
            'service_titles',
            'services',
            'review',
            'created_at'
        )

    def create(self, validated_data):
        service_titles = validated_data.pop('service_titles', [])
        application_form = ApplicationForm.objects.create(**validated_data)
        services = Service.objects.filter(title__in=service_titles)
        application_form.service.set(services)
        return application_form
