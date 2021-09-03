from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from system import views as system_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),
    path('todo/', include('todo.urls')),
    path('file/', include('file.urls')),
    path('wifi/', include('wifi.urls')),
    path('sensors/', include('sensors.urls')),

  	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/get-groups/', system_views.getUserGroups),
    path('api/ec2-server/',system_views.ec2Server),
]
