from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Social
from .serializers import SocialSerializer, SocialDetailSerializer


class SocialList(generics.ListCreateAPIView):
    """
    List all social media links
    Create a new social media link if authenticated
    Associate the current logged in user with the social media link
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        # get social media links on each profile
        'profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a social media link
    update or delete a social media link if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SocialDetailSerializer
    queryset = Social.objects.all()
