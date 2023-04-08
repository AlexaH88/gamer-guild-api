from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    """
    Chat model, related to User
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chatter'
        )
    chattee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chattee', default=1
        )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.chattee}'
