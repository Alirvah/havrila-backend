from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Online(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_online_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_online_update', args=(self.pk,))

