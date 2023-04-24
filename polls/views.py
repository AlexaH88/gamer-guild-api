from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Poll
from .serializers import PollSerializer, PollDetailSerializer


class PollList(generics.ListCreateAPIView):
    """
    List all polls
    Create a new poll if authenticated
    Associate the current logged in user with the poll
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        # get polls on each event
        'event',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poll
    update or delete a poll if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()
