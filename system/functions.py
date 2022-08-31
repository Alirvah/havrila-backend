from system import models as systemModels
import datetime
from django.utils.timezone import make_aware
import boto3
import requests
import json
from django.conf import settings
import uuid


#def archiveWorld():
#    s3 = boto3.resource('s3')
#    bucket = s3.Bucket('<bucket>')
#    newestFile = [i.key for i in bucket.objects.filter(Delimiter="/")][-1]
#    s3.meta.client.copy({'Bucket':'<bucket>','Key':newestFile},'<folder>','<file>')


def stopIfEmpty():
    ec2 = boto3.resource('ec2')
    aws = systemModels.Setting.objects.get(name='aws')
    instance = ec2.Instance(aws.data['server']['minecraft'])
    online = systemModels.Online.objects.all().first()
    now = datetime.datetime.now()
    oneHourOld = make_aware(now-datetime.timedelta(hours=1))
    if online.created_at < oneHourOld:
        if instance.state['Name'] == 'running':
            instance.stop()
            sl = systemModels.Server_log(
              name = uuid.uuid4(),
              user = 'automat',
              operation = 'stopped',
              server = 'minecraft',
            )
            sl.save()


def stopValheimIfEmpty():
    gte = make_aware(datetime.datetime.now())-datetime.timedelta(minutes=20)
    serverJustStarted = systemModels.Data.objects.filter(name='valheim',data='started',last_updated__gte=gte)
    if not serverJustStarted:
        ec2 = boto3.resource('ec2')
        aws = systemModels.Setting.objects.get(name='aws')
        instance = ec2.Instance(aws.data['server']['valheim'])
        url = f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={settings.STEAM_KEY}&filter=%5Caddr%5C{instance.public_ip_address}'
        response = json.loads(requests.get(url).text)
        if instance.state['Name'] == 'running':
            if response and 'servers' in response['response']:
                if response['response']['servers'][0]['players'] == 0:
                    instance.stop()
                    sl = systemModels.Server_log(
                      name = uuid.uuid4(),
                      user = 'automat',
                      operation = 'stopped',
                      server = 'valheim',
                    )
                    sl.save()
    lte = make_aware(datetime.datetime.now())-datetime.timedelta(hours=20)
    serverIsRunningTooLong = systemModels.Data.objects.filter(name='valheim',data='started',last_updated__lte=lte)
    if serverIsRunningTooLong:
        ec2 = boto3.resource('ec2')
        aws = systemModels.Setting.objects.get(name='aws')
        instance = ec2.Instance(aws.data['server']['valheim'])
        if instance.state['Name'] == 'running':
            instance.stop()
            sl = systemModels.Server_log(
              name = uuid.uuid4(),
              user = 'automat',
              operation = 'stopped',
              server = 'valheim',
            )
            sl.save()

def restoreArchivedServer(server):
    game = server
    
    VALHEIM = 'valheim'
    MINECRAFT = 'minecraft'
    
    ec2 = boto3.client('ec2')
    
    images = ec2.describe_images(Owners=['self'],Filters=[{'Name':'description','Values':[game]}])
    ami_of_latest_image = images['Images'][0]['ImageId']
    
    sg = ec2.describe_security_groups( Filters=[{'Name':'group-name','Values':[f'{game}*']}])
    security_group = sg['SecurityGroups'][0]['GroupId']
    
    
    instance_type = 'unknown'
    if game == VALHEIM:
        instance_type = 't3.medium'
    if game == MINECRAFT:
        instance_type = 't3.small'

    #print(ami_of_latest_image,security_group,instance_type)

    resp=ec2.run_instances(
        ImageId=ami_of_latest_image,
        InstanceType=instance_type,
        KeyName='minecraftServer',
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeviceIndex': 0,
                'SubnetId': 'subnet-0248ac2bc396e797d',
                'Groups': [security_group]
            }
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': game
                    },
                ]
            },
        ],
    )
    #print(resp['Instances'][0]['InstanceId'])




    
