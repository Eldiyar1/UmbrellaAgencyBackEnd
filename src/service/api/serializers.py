from rest_framework import serializers
from service import models as service_mod


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_mod.Section
        fields = (
            'id',
            'title',
            'description'
        )


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_mod.Process
        fields = (
            'id',
            'description'
        )


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_mod.Portfolio
        fields = (
            'id',
            'img',
            'title'
        )


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_mod.TeamMember
        fields = (
            'id',
            'position'
        )


class TabSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    processes = ProcessSerializer(many=True)
    portfolios = PortfolioSerializer(many=True)
    team = TeamMemberSerializer(many=True)

    class Meta:
        model = service_mod.Tab
        fields = (
            'id',
            'title',
            'sections',
            'processes',
            'portfolios',
            'team'
        )


class ServiceSerializer(serializers.ModelSerializer):
    tabs = TabSerializer(many=True)

    class Meta:
        model = service_mod.Service
        fields = (
            'id',
            'title',
            'gif',
            'short_description_for_banner',
            'tabs'
        )


class ServiceMainPageSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = service_mod.Service
        fields = (
            'id',
            'title',
            'category'
        )

    def get_title(self, obj):
        return obj.title

    def get_category(self, obj):
        return [{'id': tab.id, 'title': tab.title} for tab in obj.tabs.all()]
