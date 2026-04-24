from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'message': 'Welcome to the raihanstack E-Commerce API',
        'version': '1.0.0',
        'status': 'Running',
        'endpoints': {
            'auth': {
                'register': reverse('register', request=request, format=format),
                'login': reverse('login', request=request, format=format),
                'token_refresh': reverse('token_refresh', request=request, format=format),
                'profile': reverse('profile', request=request, format=format),
            },
            'products': {
                'list': reverse('product-list', request=request, format=format),
                'categories': reverse('category-list', request=request, format=format),
            },
            'orders': {
                'list': reverse('order-list', request=request, format=format),
                'cart': reverse('cart-mine', request=request, format=format),
            },
            'documentation': {
                'swagger': reverse('swagger-ui', request=request, format=format),
                'redoc': reverse('redoc', request=request, format=format),
            }
        }
    })

def home(request):
    return render(request, 'home.html')
