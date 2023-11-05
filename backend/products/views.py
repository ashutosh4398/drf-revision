from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        # we can customize our queryset here...
        return super().get_queryset()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def perform_update(self, serializer):   
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        return super().perform_update(serializer)

class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class ProductCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # customization
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(content=content)

product_create_view = ProductCreateApiView.as_view()


@api_view(['GET', 'POST'])
def product_all_views(request, id=None, *args, **kwargs):
    if request.method == "GET":
        if id is not None:
            # detail view
            product = get_object_or_404(Product, id=id)
            data = ProductSerializer(product).data
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        title = validated_data.get("title")
        content = validated_data.get("content")
        if content is None:
            content = title
        instance = serializer.save(content=content)
        print(instance)
        return Response(serializer.data)


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        if kwargs.get("id"):
            return super().retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    

