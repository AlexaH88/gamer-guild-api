from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer


class ReplyList(generics.ListCreateAPIView):
    """
    List replies or create a reply if logged in.
    """
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reply.objects.all()

    # use generics in-built perform_create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# update API View not included as replies don't need to be updated
class ReplyDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a reply or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
