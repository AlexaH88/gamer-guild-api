from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model, related to User
    Default image set so that we can always reference image.url.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    xbox = models.URLField(blank=True)
    playstation = models.URLField(blank=True)
    steam = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitch = models.URLField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_iu6lgr', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
