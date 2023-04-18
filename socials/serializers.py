from rest_framework import serializers
from .models import Social


class SocialSerializer(serializers.ModelSerializer):
    """
    Social serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Social
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'profile', 'xbox',
            'playstation', 'steam', 'discord', 'youtube', 'twitch', 'is_owner',
        ]
