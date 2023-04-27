from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Discussion(models.Model):
    """
    Discussion model, related to User and Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='discussions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.content}'
