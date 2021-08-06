from rest_framework import serializers
from ..models import Pizza, Size, Topping


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer for Pizza"""

    class Meta:
        model = Pizza
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    """Serializers for Pizza Size"""

    class Meta:
        model = Size
        fields = "__all__"


class ToppingSerializer(serializers.ModelSerializer):
    """Serializers for Pizza Topping"""

    class Meta:
        model = Topping
        fields = "__all__"
