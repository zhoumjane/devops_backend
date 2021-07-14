from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework import serializers

User = get_user_model()


class PermissionSerializer(serializers.ModelSerializer):
    """
        Permission serialization class for a model.
    """
    class Meta:
        model = Permission
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    """
        Group serialization class for a model.
    """
    permissions = PermissionSerializer(many=True)
    def to_representation(self, instance):
        member = instance.user_set.count()
        ret = super(GroupSerializer, self).to_representation(instance)
        ret["member"] = member
        return ret

    class Meta:
        model = Group
        fields = "__all__"


class GroupWriteSerializer(serializers.ModelSerializer):
    """
        Group serialization class for a model.
    """
    class Meta:
        model = Group
        fields = "__all__"