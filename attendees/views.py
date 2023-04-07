from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Attend
from .serializers import AttendeeSerializer


class AttendeeList(generics.ListCreateAPIView):
    """
    Attendee list view
    """
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Attend.objects.all()

    # use generics in-built perform_create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# update API View not included as attends don't need to be updated
class AttendeeDetail(generics.RetrieveDestroyAPIView):
    """
    Attendee detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendeeSerializer
    queryset = Attend.objects.all()
