from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Social(models.Model):
    """
    Social model, related to User and Profile
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    xbox = models.URLField(blank=True)
    playstation = models.URLField(blank=True)
    steam = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitch = models.URLField(blank=True)

    class Meta:
        ordering = [
            'discord',
            'playstation',
            'steam',
            'twitch',
            'xbox',
            'youtube',
        ]

    def __str__(self):
        return f"{self.owner}'s social media channels"
