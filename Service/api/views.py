from rest_framework import generics, permissions
from rest_framework.views import APIView

from Service.api.models import Product, Profile, Category, Cart
from Service.api.serializers import ProductSerializer, CartAddSerializer


class ProductxView(APIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer()

class CartAddView(generics.CreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartAddSerializer()
    permission_classes = (permissions.IsAuthenticated, )


