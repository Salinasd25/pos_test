from rest_framework import serializers
from pos_test.models import (
    Product,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')