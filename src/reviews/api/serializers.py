from rest_framework import serializers

from reviews import models as review_mod


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review_mod.Review
        fields = (
            'avatar',
            'fullname',
            'position',
            'company_name',
            'star',
            'description',
        )
