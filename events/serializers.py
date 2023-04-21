from rest_framework import serializers
from .models import Event
from replies.models import Reply
from polls.models import Poll


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reply_id = serializers.SerializerMethodField()
    replies_count = serializers.ReadOnlyField()
    polls_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        # check for 2mb file size limit
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_reply_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reply = Reply.objects.filter(
                owner=user, event=obj
                ).first()
            return reply.id if reply else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'about',
            'image', 'is_owner', 'profile_id', 'profile_image', 'platform',
            'date', 'start_time', 'end_time', 'location', 'replies_count',
            'reply_id', 'polls_count',
        ]
