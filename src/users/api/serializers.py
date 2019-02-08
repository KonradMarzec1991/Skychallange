from django.contrib.auth.models import User
from rest_framework import serializers


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'uri']

    def get_uri(self, obj):
        return '/api/users/{id}'.format(id=obj.id)
