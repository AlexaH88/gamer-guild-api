from django.db import models
from django.contrib.auth.models import User
from polls.models import Poll


class Vote(models.Model):
    """
    Vote model, related to Poll
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='votes')
    yes = models.BooleanField(blank=True, null=True)
    maybe = models.BooleanField(blank=True, null=True)
    no = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'poll']

    def __str__(self):
        return f'{self.owner} {self.poll}'
