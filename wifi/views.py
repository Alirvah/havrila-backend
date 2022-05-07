from . import models

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def WifiPostViewSet(request, format=None):
    if 'devices' in request.data:
      for i in request.data['devices']:
        wifi = models.Device.objects.create(
               ip=i['ip'],
               mac=i['mac'],
               name=i['name']
        )
        wifi.save()
    return Response({'status':'ok'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def WifiGetViewSet(request, format=None):
    r = list(models.Device.objects.values())
    return JsonResponse({'data':r})

