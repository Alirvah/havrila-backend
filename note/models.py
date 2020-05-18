from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Note(models.Model):

    title = models.CharField(max_length=100)
    content = models.BinaryField(max_length=50**6)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    starred = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('note_note_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('note_note_update', args=(self.pk,))



