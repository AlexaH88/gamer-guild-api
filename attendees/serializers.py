from django.db import IntegrityError
from rest_framework import serializers
from .models import Attend


class AttendeeSerializer(serializers.ModelSerializer):
    """
    Attendee serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attend
        fields = [
            'id', 'owner', 'event', 'created_at'
        ]

    # check for duplicate attend
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
