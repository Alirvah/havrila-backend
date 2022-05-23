from unicodedata import name
from system import models
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from helpers.permissions import FastTokenAllow
from helpers.decorators import isInGroup
import time
from django.conf import settings
import boto3
import uuid
import json
import requests


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserGroups(request):
  return Response({'groups':[g.name for g in request.user.groups.all()]})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@isInGroup(['minecraft','valheim','workadventure'])
def ec2Server(request):
  ec2 = boto3.resource('ec2')
  aws = models.Setting.objects.get(name='aws')
  instance = ec2.Instance(aws.data['server'][request.data['instance']])

  if 'action' not in request.data:
    return Response({'status':'nothing to do'})

  inst_type = [i for i in aws.data['instances'] if instance.instance_type in i]
  if request.data['action'] == 'state':
    response = {
      'status':instance.state['Name'],
      'type': inst_type[0] if inst_type else '',
      'ip':instance.public_ip_address
    }
    return Response(response)

  if request.data['action'] == 'start':
    if instance.state['Name'] == 'stopped':
      instance.start()
      sl = models.Server_log(
        name = uuid.uuid4(),
        user = request.user.username,
        operation = 'started',
        server = request.data['instance'],
      )
      sl.save()
      valheimServerData, created = models.Data.objects.get_or_create(
        name='valheim',
        data='started'
      )
      valheimServerData.save()
    return Response({'status':'starting...'})

  if request.data['action'] == 'stop':
    if request.data['instance'] == 'valheim':
      url = f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={settings.STEAM_KEY}&filter=%5Caddr%5C{instance.public_ip_address}'
      response = json.loads(requests.get(url).text)
      if instance.state['Name'] == 'running':
        if response and 'servers' in response['response']:
          if response['response']['servers'][0]['players'] == 0:
            instance.stop()
            sl = models.Server_log(
              name = uuid.uuid4(),
              user = request.user.username,
              operation = 'stopped',
              server = 'valheim',
            )
            sl.save()
            return Response({'status':'stopping...'})
    else:
      if instance.state['Name'] == 'running':
        instance.stop()
        sl = models.Server_log(
          name = uuid.uuid4(),
          user = request.user.username,
          operation = 'stopped',
          server = request.data['instance'],
        )
        sl.save()
        return Response({'status':'stopping...'})

  return Response({'status':'nothing to do'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@isInGroup(['minecraft','valheim','workadventure'])
def changeEc2Instance(request):
  ec2 = boto3.resource('ec2')
  aws = models.Setting.objects.get(name='aws')
  instance = ec2.Instance(aws.data['server'][request.data['instance']])

  if 'newInstance' in request.data:
    if request.data['newInstance'] in aws.data['instances']:
      if instance.state['Name'] == 'stopped':
        instance.modify_attribute(
          InstanceType={
              'Value': request.data['newInstance'].split(' = ')[0]
          }
        )
      else:
        return Response({'status':'stop machine first'},status=400)
      time.sleep(1)
      if instance.instance_type == request.data['newInstance'].split(' = ')[0]:
        sl = models.Server_log(
          name = uuid.uuid4(),
          user = request.user.username,
          operation = f'changed to {request.data["newInstance"]}',
          server = request.data['instance'],
        )
        sl.save()
        return Response({'status':'done'})
      else:
        return Response({'status':'instance type was not changed'},status=400)

  return Response({'status':'nothing to do'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@isInGroup(['minecraft','valheim','workadventure'])
def getInstanceTypes(request):
  aws = models.Setting.objects.get(name='aws')
  return Response({"types":aws.data['instances']})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@isInGroup(['minecraft'])
def getLastBackup(request):
  get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
  client = boto3.client('s3')
  objs = client.list_objects_v2(Bucket='minecraft.bak')['Contents']
  lastBackup, lastArchive = '',''
  for obj in sorted(objs, key=get_last_modified, reverse=True):
    if 'tar.gz' in obj['Key']:
        lastArchive = obj['LastModified']
    if 'world/' in obj['Key']:
        lastBackup = obj['LastModified']
    if lastBackup and lastArchive:
        break
  result = {"lastBackup":lastBackup.__str__(),"lastArchive":lastArchive.__str__()}
  return Response(result)


@api_view(['GET'])
@permission_classes([IsAuthenticated|FastTokenAllow])
def fastStart(request): 
  token = request.query_params['t']
  if token == settings.FAST_TOKEN:
    ec2 = boto3.resource('ec2')
    aws = models.Setting.objects.get(name='aws')
    instance = ec2.Instance(aws.data['server'][request.data['instance']])
    if instance.state['Name'] == 'stopped':
      instance.start()
    return Response({'status':'starting...'})
  return Response('Ops!',status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated|FastTokenAllow])
def fastStop(request):
  token = request.query_params['t']
  if token == settings.FAST_TOKEN:
    ec2 = boto3.resource('ec2')
    aws = models.Setting.objects.get(name='aws')
    instance = ec2.Instance(aws.data['server'][request.data['instance']])
    if instance.state['Name'] == 'running':
      instance.stop()
    return Response({'status':'stopping...'})
  return Response('Ops!',status=400)



