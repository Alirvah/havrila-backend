from note import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from system import views as system_views
from rest_framework import routers

from system import api

router = routers.DefaultRouter()
router.register(r'online', api.OnlineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),
    path('todo/', include('todo.urls')),
    path('file/', include('file.urls')),
    path('wifi/', include('wifi.urls')),
    path('sensors/', include('sensors.urls')),
    path('system/',include(router.urls)),

  	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/get-groups/', system_views.getUserGroups),
    path('api/ec2-server/',system_views.ec2Server),
    path('api/ec2-server-change-instance/',system_views.changeEc2Instance),
    path('api/ec2-server-get-instances/',system_views.getInstanceTypes),

    path('api/s3-backup/',system_views.getLastBackup),

]
