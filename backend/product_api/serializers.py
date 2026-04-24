from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'photo']
        extra_kwargs = {'photo': {'required': False, 'allow_null': True}}
        depth = 1

        def create(self, validated_data):
            product = Product.objects.create(**validated_data)
            return product
        
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.price = validated_data.get('price', instance.price)
            instance.photo = validated_data.get('photo', instance.photo)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()
            return instance