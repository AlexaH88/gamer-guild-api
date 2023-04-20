from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Member(models.Model):
    """
    Member model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'group']

    def __str__(self):
        return f'{self.owner} {self.group}'
