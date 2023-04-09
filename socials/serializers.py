from rest_framework import serializers
from .models import Social


class SocialSerializer(serializers.ModelSerializer):
    """
    Social serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    # profile = serializers.ReadOnlyField(source='profile.id')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Social
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'profile', 'xbox', 'playstation', 'steam', 'discord',
            'youtube', 'twitch',
        ]


class SocialDetailSerializer(SocialSerializer):
    """
    Social detail serializer
    """
    profile = serializers.ReadOnlyField(source='profile.id')
