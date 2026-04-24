from rest_framework import routers
from .views import ProductViewSet
from django.urls import re_path, include

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
