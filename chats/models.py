from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    """
    Chat model, related to Users
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chatter'
        )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chattee', default=1
        )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.content
