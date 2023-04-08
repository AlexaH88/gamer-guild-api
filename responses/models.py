from django.db import models
from django.contrib.auth.models import User
from chats.models import Chat


class Response(models.Model):
    """
    Response model, related to User and Chat
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='chat_response'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
