from rest_framework import serializers
from .models import Group
from members.models import Member


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    member_id = serializers.SerializerMethodField()
    events_count = serializers.ReadOnlyField()
    members_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_member_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            member = Member.objects.filter(
                owner=user, group=obj.owner
                ).first()
            return member.id if member else None
        return None

    class Meta:
        model = Group
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'about',
            'image', 'is_owner', 'events_count', 'members_count', 'website',
            'location', 'phone', 'email', 'member_id',
        ]
