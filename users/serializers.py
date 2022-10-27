from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
                "username", 
                "password", 
                "first_name", 
                "last_name", 
                "is_seller", 
                "date_joined", 
                "is_active", 
                "is_superuser"
            ]
        extra_kwargs = {'is_seller': {'required': True}}


    def create(self, validated_data:dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
                "id",
                "username", 
                "password", 
                "first_name", 
                "last_name", 
                "is_seller", 
                "date_joined", 
                "is_active", 
                "is_superuser"
            ]
        
        read_only_fields = ["is_active"]


class UserDisableSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
                "id",
                "username", 
                "password", 
                "first_name", 
                "last_name", 
                "is_seller", 
                "date_joined", 
                "is_active", 
                "is_superuser"
            ]
        
        extra_kwargs = {'is_active': {'required': True}}

        read_only_fields = [
            "id", 
            "username", 
            "password",
            "first_name", 
            "last_name", 
            "is_seller", 
            "date_joined", 
            "is_superuser"
        ]