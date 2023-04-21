from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Poll(models.Model):
    """
    Poll model, related to User and Event
    """
    class Response(models.TextChoices):
        YES = "Y"
        MAYBE = "M"
        NO = "N"

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='polls')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255, choices=Response.choices)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.content}'
