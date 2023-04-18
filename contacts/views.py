from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    """
    List contacts or create contacts if logged in.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()

    # use generics in-built perform_create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve contacts or delete them by id if you own them.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
