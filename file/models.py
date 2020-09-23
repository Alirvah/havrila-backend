from django.db import models

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Filer(models.Model):

    upload = models.FileField(upload_to=settings.MEDIA_URL)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    size = models.IntegerField(null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="filer", 
    )

    def save(self, *args, **kwargs):
        self.size = self.upload.size
        self.title = self.upload.name
        super(Filer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('file_filer_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('file_filer_update', args=(self.pk,))



