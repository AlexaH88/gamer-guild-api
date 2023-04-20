from rest_framework import serializers
from .models import Event
from likes.models import Like
from attendees.models import Attend
from comments.models import Comment


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    attend_id = serializers.SerializerMethodField()
    comment_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    attendees_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, event=obj
                ).first()
            return like.id if like else None
        return None

    def get_attend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attend = Attend.objects.filter(
                owner=user, event=obj
                ).first()
            return attend.id if attend else None
        return None

    def get_comment_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment = Comment.objects.filter(
                owner=user, event=obj
                ).first()
            return comment.id if comment else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'about',
            'image', 'is_owner', 'profile_id', 'profile_image', 'like_id',
            'attend_id', 'comments_count', 'likes_count', 'attendees_count',
            'comment_id', 'platform', 'date', 'start_time', 'end_time',
            'location',
        ]
