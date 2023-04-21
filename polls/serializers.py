from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    """
    Poll serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    choices = serializers.ChoiceField(choices='poll.response_choices')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # change standard time format from 02 Aug 2021 eg to how many minutes ago
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Poll
        fields = [
            'id', 'owner', 'event', 'created_at', 'updated_at',
            'response', 'is_owner', 'profile_id', 'profile_image'
        ]


class PollDetailSerializer(PollSerializer):
    """
    Poll detail serializer
    """
    event = serializers.ReadOnlyField(source='event.id')
