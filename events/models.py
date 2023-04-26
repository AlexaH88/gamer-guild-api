from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    platform = models.URLField(blank=True)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    location = models.TextField(blank=True)
    organiser = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_xh1cpv', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
