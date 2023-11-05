import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# NORMAL DJANGO VIEW
# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest parsed by django and passed to api function
#     data = {}
#     model_data: Product = Product.objects.order_by("?").first()
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title", "price"])
#         print(data) # PAIN POINT: NOT ALL TYPES ARE JSON SERIALIZABLE
#         # {'id': 1, 'title': 'One Plus fitbit', 'price': Decimal('1000.00')}
#         # serialization
#     return JsonResponse(data)


# DRF VIEW
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    print(request.data)
    data = {}
    instance: Product = Product.objects.order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    
    return Response(request.data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # DATA VALIDATION USING SERIALIZER

    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    print(instance)
    return Response(serializer.data)