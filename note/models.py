from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)
    pinned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pinned', 'position', 'created_at']

    def __str__(self):
        return self.title