from django.db import IntegrityError
from rest_framework import serializers
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):
    """
    Reply serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reply
        fields = [
            'id', 'owner', 'event', 'created_at', 'event_choices',
        ]

    # check for duplicate reply
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
