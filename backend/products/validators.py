from .models import Product
from rest_framework import serializers

def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is alrady a product name")
    return value