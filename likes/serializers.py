from django.db import IntegrityError
from rest_framework import serializers
from .models import Like
from posts.models import Post
from events.models import Event


class LikeSerializer(serializers.ModelSerializer):
    """
    Like serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(
        allow_null=True, required=False, queryset=Post.objects.all()
    )
    event = serializers.PrimaryKeyRelatedField(
        allow_null=True, required=False, queryset=Event.objects.all()
    )

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post', 'event', 'created_at'
        ]

    # check for duplicate like
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
