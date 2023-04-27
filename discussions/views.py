from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Discussion
from .serializers import DiscussionSerializer, DiscussionDetailSerializer


class DiscussionList(generics.ListCreateAPIView):
    """
    List all discussions
    Create a new discussion if authenticated
    Associate the current logged in user with the discussion
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DiscussionSerializer
    queryset = Discussion.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        # get discussions on each event
        'event',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a discussion
    update or delete a discussion if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DiscussionDetailSerializer
    queryset = Discussion.objects.all()
