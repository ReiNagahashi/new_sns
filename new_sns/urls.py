from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    path('api/token-auth/',obtain_jwt_token),
    path('api/token-refresh/', refresh_jwt_token),
    path('api/token-verify/', verify_jwt_token),
    path('api/accounts/',include('accounts.urls')),
    path('api/problems/',include('problem.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
