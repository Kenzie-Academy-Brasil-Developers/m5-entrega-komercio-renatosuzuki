from rest_framework import serializers
from .models import Product
from users.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["description", "price", "quantity", "is_active", "seller_id"]


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                "id",
                "username",  
                "first_name", 
                "last_name", 
                "is_seller", 
                "date_joined", 
                "is_active", 
                "is_superuser"
            ]


class ProductDetailedSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    
    
    class Meta:
        model = Product
        fields = ["id", "seller", "description", "price", "quantity", "is_active"]
        extra_kwargs = {'description': {'required': True}}
        extra_kwargs = {'price': {'required': True}}
        extra_kwargs = {'quantity': {'required': True}}


class ProductGetDetailSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)


    class Meta:
        model = Product
        fields = ["seller", "description", "price", "quantity", "is_active"]