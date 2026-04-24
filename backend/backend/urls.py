from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from user_api.views import UserObtainToken

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include('user_api.urls')),
    re_path(r'^auth/?$', UserObtainToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
