from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    events_count = serializers.ReadOnlyField()
    members_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Group
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'about',
            'image', 'is_owner', 'events_count', 'members_count',
        ]
