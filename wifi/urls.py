from django.urls import path

from . import views

urlpatterns = (
    path('api/v1/wifi/post/', views.WifiPostViewSet),
    path('api/v1/wifi/get/', views.WifiGetViewSet),
)


