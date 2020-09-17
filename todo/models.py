from django.db import models
from django.conf import settings
from django.utils import timezone

class Todo(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="todo", 
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('todo_todo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('todo_todo_update', args=(self.pk,))


