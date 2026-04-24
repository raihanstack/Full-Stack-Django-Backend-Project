from rest_framework import routers
from .views import ProductViewSet, CartItemViewSet
from django.urls import re_path, include

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register('cart-items', CartItemViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
