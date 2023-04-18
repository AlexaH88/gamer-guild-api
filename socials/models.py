from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Social(models.Model):
    """
    Social model, related to User and Profile
    """
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    xbox = models.URLField(blank=True)
    playstation = models.URLField(blank=True)
    steam = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitch = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s socials"
