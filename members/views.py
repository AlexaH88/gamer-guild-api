from rest_framework import generics, permissions
from gamer_guild_api.permissions import IsOwnerOrReadOnly
from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    """
    List all members, i.e. all users that are members of the group
    Create a membership, i.e. become a member of a group if logged in
    Perform_create: associate the current logged in user with a group
    """
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Member.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MemberDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a member
    No Update view, as we either join or leave the group
    Destroy a member, i.e. leave the group if owner
    """
    serializer_class = MemberSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Member.objects.all()
