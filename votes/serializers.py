from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Vote serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = [
            'id', 'owner', 'poll', 'created_at', 'yes', 'maybe', 'no'
        ]

    # check for duplicate vote
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
