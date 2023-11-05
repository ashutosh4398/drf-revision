from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(method_name="get_my_discount")
    
    class Meta:
        model = Product
        fields = [
            "title", 
            "content", 
            "price", 
            "sale_price",
            "my_discount",
        ]

    
    def get_my_discount(self, instance: Product):
        try:
            return instance.get_discount()
        except: 
            # during post request, instance=OrderedDict, which is causing issue
            return None