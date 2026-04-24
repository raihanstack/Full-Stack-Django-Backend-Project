from rest_framework import routers
from .views import UserViewSet
from django.urls import re_path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
