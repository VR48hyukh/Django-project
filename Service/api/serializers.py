from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_object_or_404
from Service.Document.models import Sensor
from Service.api.models import Product, Category, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name', )


class CartSerializer(serializers.ModelSerializer):
    product=ProductSerializer()

    class Meta:
        model=Cart
        fields=('id','count', 'product',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    image=serializers.ImageField(source='profile.image')

class CartAddSerializer(serializers.ModelSerializer):
    product_id=serializers.IntegerField()
    def create(self, validated_data):
        user=User.objects.get(id=self.context['request'].user.id)
        #request=self.context.get('request')
        #user_id=request.user.id
        product=get_object_or_404(Product, id=validated_data['product_id'])
        if product.count==0 or product.is_available==False:
            raise serializers.ValidationError({'not availabe':'the product is not avalable'})

        cart=Cart.objects.creat(
            product=product,
            user=user,
            count=validated_data['count'],

        )
        cart.save()





