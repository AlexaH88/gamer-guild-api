from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Chat serializer
    """
    # owner = serializers.SlugRelatedField(
    #     many=False, slug_field='username', queryset=User.objects.all()
    # )
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    receiver = serializers.SlugRelatedField(
        many=False, slug_field='username', queryset=User.objects.all()
    )
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.profile.id')
    owner_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    receiver_id = serializers.ReadOnlyField(
        source='receiver.profile.id'
    )
    receiver_image = serializers.ReadOnlyField(
        source='receiver.profile.image.url'
    )
    created_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # change standard time format from 02 Aug 2021 eg to how many minutes ago
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Chat
        fields = [
            'id', 'owner', 'receiver', 'content', 'created_at', 'is_read',
            'is_owner', 'owner_id', 'owner_image', 'receiver_id',
            'receiver_image'
        ]
