from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """
        Server serializer class for a model.
    """
    last_check = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True, help_text="检查时间")
    last_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", help_text="到期时间")

    def to_representation(self, instance):
        ret = super(ServerSerializer, self).to_representation(instance)
        owner_list = list(instance.owner.all().values("id", "username"))
        ret['owner'] = owner_list
        return ret

    class Meta:
        model = Server
        fields = '__all__'

