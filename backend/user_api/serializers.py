from rest_framework import serializers
from .models import SiteUser
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = SiteUser
        fields = ['username', 'email', 'password', 'confirm_password', 'role', 'phone_number', 'shipping_address']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'shipping_address', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)