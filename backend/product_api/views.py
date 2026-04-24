from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.response import Response
from .models import CartItem, Product
from .serializers import CartItemSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({'error': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if item already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:
            # If it exists, just add the quantity
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )

    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()