from system import models as systemModels
import datetime
from django.utils.timezone import make_aware
import boto3

def archiveWorld():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('minecraft.bak')
    newestFile = [i.key for i in bucket.objects.filter(Delimiter="/")][-1]
    s3.meta.client.copy({'Bucket':'minecraft.bak','Key':newestFile},'minecraft-world-download','test.tar.gz')


INSTANCE_ID = 'i-07d6d549d3b5cdb92'
EC2 = 'ec2'

def stopServer():
    ec2 = boto3.resource(EC2)
    instance = ec2.Instance(INSTANCE_ID)
    instance.stop()


def startServer():
    ec2 = boto3.resource(EC2)
    instance = ec2.Instance(INSTANCE_ID)
    instance.start()


def getServerState():
    ec2 = boto3.resource(EC2)
    instance = ec2.Instance(INSTANCE_ID)
    return instance.state['Name']


def stopIfEmpty():
    online = systemModels.Online.objects.all().first()
    now = datetime.datetime.now()
    oneHourOld = make_aware(now-datetime.timedelta(hours=1))
    if online.created_at < oneHourOld:
        if getServerState() == 'running':
            stopServer()