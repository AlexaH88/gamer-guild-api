from django.db import IntegrityError
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Member serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Member
        fields = [
            'id', 'owner', 'group', 'created_at', 'group_name',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
