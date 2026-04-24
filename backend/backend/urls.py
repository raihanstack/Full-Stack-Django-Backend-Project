from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from user_api.views import UserObtainToken

from .views import api_root, home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    re_path(r'^api/', include('user_api.urls')),
    re_path(r'^api/', include('product_api.urls')),
    re_path(r'^auth/?$', UserObtainToken.as_view(), name='auth_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
