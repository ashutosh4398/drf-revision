from rest_framework import serializers
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class UserPublicDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    products = ProductSerializer(read_only=True, source="product_set.all", many=True)
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "id",
            "products"
        ]

