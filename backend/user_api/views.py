from .models import SiteUser
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
class UserObtainToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)

        checkUser = SiteUser.objects.filter(username=username)
        if not checkUser.exists():           
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = super().post(request, *args, **kwargs)
        if response.status_code != status.HTTP_200_OK:
            return response

        token = response.data.get('token')
        user = SiteUser.objects.get(username=username)
        serializer = UserSerializer(user)

        return Response({
            'token': token,
            'user': serializer.data
        })