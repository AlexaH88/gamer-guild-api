from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    Group model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.TextField(blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_l8giye', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
