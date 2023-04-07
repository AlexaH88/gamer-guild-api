from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from events.models import Event


class Comment(models.Model):
    """
    Comment model, related to User, Post and Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comments'
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='event_comments',
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
