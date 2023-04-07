from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from events.models import Event


class Like(models.Model):
    """
    Like model, related to User, Post and Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_likes'
        )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='event_likes',
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner}'
