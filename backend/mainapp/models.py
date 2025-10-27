from django.db import models
from django.utils.text import slugify
from django.db.models import UniqueConstraint

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200)
    session_key = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"ID: {self.pk} | {self.title}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    class Meta:
        ordering = ['done']
        constraints = [
            UniqueConstraint(fields=['slug', 'session_key'], name='unique_slug_per_session')
        ]
        