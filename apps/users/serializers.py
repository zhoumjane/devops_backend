from rest_framework import serializers
from django.contrib.auth.models import User, Group
from groups.serializers import PermissionSerializer


class GroupSerializer(serializers.ModelSerializer):
    """
        Group serializer class for a model.
    """
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """
        User serializer class for a model.
    """

    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "groups", "email", "user_permissions")


class UserWriteSerializer(serializers.ModelSerializer):
    """
        User Write serializer class for a model.
    """
    class Meta:
        model = User
        fields = ("groups","user_permissions")

