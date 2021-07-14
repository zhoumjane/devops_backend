from .serializers import ImageSerializer
from .models import Image
from rest_framework import viewsets, mixins, filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from utils.pagination import Pagination
from utils.filters import ImagesFilter
from django_filters.rest_framework import DjangoFilterBackend
from .tasks import sync_image
from rest_framework.response import Response
from rest_framework import status


class ImageViewSet(CacheResponseMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
        Create a model instance.
        Retrieve a model instance.
        List all model instance.
    """
    queryset = Image.objects.all().order_by("-commit_time")
    serializer_class = ImageSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("commit_id", "image_name", "owner", "commit_time", "status", "url", "branch")
    filter_class = ImagesFilter
    search_fields = ("commit_id", "image_name", "owner", "status", "url", "branch")

    # Create a model instance.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        sync_image.delay(serializer.data['image_name'], serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)