from rest_framework import serializers

from portfolio import models as port_mod


class PortfolioSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%m-%d-%Y')

    class Meta:

        model = port_mod.Portfolio
        fields = (
            'id',
            'title',
            'price',
            'image',
            'created_at'
        )
