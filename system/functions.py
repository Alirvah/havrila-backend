from system import models as systemModels
import datetime
from django.utils.timezone import make_aware
import boto3
import requests
import json
from django.conf import settings

def archiveWorld():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('minecraft.bak')
    newestFile = [i.key for i in bucket.objects.filter(Delimiter="/")][-1]
    s3.meta.client.copy({'Bucket':'minecraft.bak','Key':newestFile},'minecraft-world-download','test.tar.gz')


def stopIfEmpty():
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(settings.INSTANCE['minecraft'])
    online = systemModels.Online.objects.all().first()
    now = datetime.datetime.now()
    oneHourOld = make_aware(now-datetime.timedelta(hours=1))
    if online.created_at < oneHourOld:
        if instance.state['Name'] == 'running':
            instance.stop()


def stopValheimIfEmpty():
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(settings.INSTANCE['valheim'])
    url = f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={settings.STEAM_KEY}&filter=%5Caddr%5C{instance.public_ip_address}'
    response = json.loads(requests.get(url).text)
    if instance.state['Name'] == 'running':
        if response and 'servers' in response['response']:
            if response['response']['servers'][0]['players'] == 0:
               instance.stop()
