from rest_framework import generics, permissions, filters
from gamer_guild_api.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from .models import Chat
from .serializers import ChatSerializer


class ChatList(generics.ListCreateAPIView):
    """
    List all chats belonging to logged in user
    Create a new chat if authenticated
    Associate the current logged in user with the chat
    """
    permission_classes = [IsOwner]
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    # for SearchFilter
    search_fields = [
        'owner__username',
        'chattee__username',
        'content'
    ]
    # for DjangoFilterBackend
    filterset_fields = [
        # filter chats from followers
        'owner__chattee__owner__profile',
        # filter user chats
        'owner__profile'
    ]

    # def get_queryset(self):
    #     """
    #     Returns a list of chats belonging to the logged in user only
    #     """
    #     user = self.request.user
    #     return Chat.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
