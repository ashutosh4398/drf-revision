from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(method_name="get_my_discount")
    detail_url = serializers.SerializerMethodField(method_name="get_detail_url")
    edit_url = serializers.HyperlinkedIdentityField(view_name="product-edit", lookup_field="id")
    email = serializers.EmailField(write_only=True)
    
    class Meta:
        model = Product
        fields = [
            "detail_url",
            "edit_url",
            "title", 
            "content", 
            "price", 
            "sale_price",
            "my_discount",
            "email"
        ]
        
    
    def get_detail_url(self, instance: Product):
        # return f"/api/products/{instance.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"id": instance.id}, request=request)

    
    def get_my_discount(self, instance: Product):
        try:
            return instance.get_discount()
        except: 
            # during post request, instance=OrderedDict, which is causing issue
            return None
    
    def update(self, instance, validated_data):
        instance.title = "MODIFIED FROM SERIALIZER"
        instance.save()
        return instance
    
    def create(self, validated_data):
        # email = validated_data.pop("email", "")
        # if email:
        #     print("SENDING EMAIL...")
        return super().create(validated_data)