from rest_framework import generics, permissions, filters
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Group
from .serializers import GroupSerializer


class GroupList(generics.ListCreateAPIView):
    """
    List all groups.
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.annotate(
        events_count=Count('owner__event', distinct=True),
        members_count=Count('owner__member', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'events_count',
        'members_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a group and edit or delete it if you own it.
    """
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Group.objects.annotate(
        events_count=Count('owner__event', distinct=True),
        members_count=Count('owner__member', distinct=True)
    ).order_by('-created_at')
