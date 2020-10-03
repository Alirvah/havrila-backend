from django.db import models

from django.utils import timezone


class Device(models.Model):

    ip = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('wifi_device_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('wifi_device_update', args=(self.pk,))


