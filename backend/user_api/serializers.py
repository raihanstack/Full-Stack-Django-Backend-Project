from rest_framework import serializers
from rest_framework.authentication.models import Token
from .models import SiteUser

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SiteUser
        fields = ['id', 'username', 'email', 'password', 'shipping_address', 'phone_number', 'special_user']
        extra_kwargs = {'password': {'write_only': True}, 'shipping_address': {'required': False}, 'phone_number': {'required': False}, 'special_user': {'required': False}}
        depth = 1

    def create(self, validated_data):
        user = SiteUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user