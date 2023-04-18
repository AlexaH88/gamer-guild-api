from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Contact serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Contact
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'group', 'website',
            'phone', 'location', 'email', 'is_owner',
        ]
