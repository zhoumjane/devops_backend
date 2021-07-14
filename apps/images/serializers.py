from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    """
        Image serializer class for a model.
    """
    commit_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True, help_text="上传时间")

    class Meta:
        model = Image
        fields = '__all__'

