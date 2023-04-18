from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Social
from .serializers import SocialSerializer


class SocialList(generics.ListCreateAPIView):
    """
    List socials or create socials if logged in.
    """
    serializer_class = SocialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Social.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SocialDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve socials or delete them by id if you own them.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
