from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.utils import timezone


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    platform = models.URLField(blank=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta)
    location = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_event_dseibs', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
