from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Chat serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    chatted_name = serializers.ReadOnlyField(source='chatted.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # change standard time format from 02 Aug 2021 eg to how many minutes ago
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Chat
        fields = [
            'id', 'owner', 'chatted', 'chatted_name', 'content', 'created_at',
            'is_owner', 'profile_id', 'profile_image', 'created_at',
            'updated_at',
        ]
