from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
import jsonfield


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


class Server_log(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=100)
    operation = models.CharField(max_length=100)
    server = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_server_log_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_server_log_update', args=(self.pk,))


class Data(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    data = models.TextField(max_length=100)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_data_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_data_update', args=(self.pk,))


class Antik_fup(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    date = models.CharField(max_length=100,unique=True)
    download = models.CharField(max_length=100)
    upload = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return '%s' % self.date

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_antik_fup_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_antik_fup_update', args=(self.pk,))


class Meeting(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    time = models.CharField(max_length=100)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_meetings_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_meetings_update', args=(self.pk,))


class Setting(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    data = jsonfield.JSONField()
    notes = models.TextField(default="")

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('system_settings_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('system_settings_update', args=(self.pk,))