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
            'auth': reverse('auth_token', request=request, format=format),
            'users': reverse('siteuser-list', request=request, format=format),
            'products': reverse('product-list', request=request, format=format),
            'cart-items': reverse('cartitem-list', request=request, format=format),
        }
    })

def home(request):
    return render(request, 'home.html')
