from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('event_comments', distinct=True),
        likes_count=Count('event_likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    # for OrderingFilter
    ordering_fields = [
        'comments_count',
        'likes_count',
        'post_likes__created_at'
    ]
    # for SearchFilter
    search_fields = [
        'owner__username',
        'title'
    ]
    # for DjangoFilterBackend
    filterset_fields = [
        # filter events from followers
        'owner__followed__owner__profile',
        # filter user events
        'owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('owner__comment', distinct=True),
        likes_count=Count('owner__like', distinct=True)
    ).order_by('-created_at')
