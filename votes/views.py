from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Vote
from .serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    """
    List votes or create a vote if logged in.
    """
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Vote.objects.all()

    # use generics in-built perform_create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a vote or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
