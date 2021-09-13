from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Sensor(models.Model):

    ts = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    broadband = models.FloatField()
    infrared = models.FloatField()
    light = models.FloatField()
    temprpi = models.FloatField()
    temproom = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.ts

    def __unicode__(self):
        return u'%s' % self.ts

    def get_absolute_url(self):
        return reverse('sensor_sensor_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('sensor_sensor_update', args=(self.pk,))


class Status(models.Model):

    ts = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    uptime = models.IntegerField()
    cpu = models.FloatField()
    mem = models.FloatField()
    disk = models.IntegerField()
    temp = models.FloatField()
    wrec = models.IntegerField()
    wtran = models.IntegerField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.ts

    def __unicode__(self):
        return u'%s' % self.ts

    def get_absolute_url(self):
        return reverse('sensor_status_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('sensor_status_update', args=(self.pk,))

