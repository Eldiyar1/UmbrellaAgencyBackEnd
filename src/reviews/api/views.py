from rest_framework import generics

from reviews.api import serializers as review_ser
from reviews import models as review_mod


class ReviewListAPIView(generics.ListAPIView):
    queryset = review_mod.Review.objects.all()
    serializer_class = review_ser.ReviewSerializer

