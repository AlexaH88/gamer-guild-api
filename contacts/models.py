from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Contact(models.Model):
    """
    Contact model, related to User and Group
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.URLField(blank=True)
    location = models.TextField(blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.group}'
