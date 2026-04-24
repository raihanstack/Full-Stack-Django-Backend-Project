from django.shortcuts import render
from .models import SiteUser
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.all()
    serializer_class = UserSerializer
