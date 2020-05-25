#from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Notebook(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="notebook", 
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('note_notebook_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('note_notebook_update', args=(self.pk,))



class Note(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    starred = models.BooleanField(default=False)

    notebook = models.ForeignKey(
        'note.Notebook',
        default=None,
        on_delete=models.CASCADE, related_name="note", 
    )

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

