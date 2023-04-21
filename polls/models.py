from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Poll(models.Model):
    """
    Poll model, related to User and Event
    """
    response_choices = [
        ('yes', 'Yes'),
        ('maybe', 'Maybe'),
        ('no', 'No'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='polls'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    response = models.CharField(
        max_length=255, choices=response_choices, default='yes'
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.content}'
