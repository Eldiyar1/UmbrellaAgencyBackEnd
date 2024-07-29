from rest_framework import serializers

from about import models as about_mod


class FounderSerializer(serializers.ModelSerializer):

    class Meta:
        model = about_mod.Founder
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = about_mod.Vacancy
        fields = '__all__'