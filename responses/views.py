from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Response
from .serializers import ResponseSerializer, ResponseDetailSerializer


class ResponseList(generics.ListCreateAPIView):
    """
    List all responses
    Create a new response if authenticated
    Associate the current logged in user with the response
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        # get comments on each chat
        'chat',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a response
    update or delete a response if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ResponseDetailSerializer
    queryset = Response.objects.all()
