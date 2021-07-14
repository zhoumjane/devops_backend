from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters, mixins
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .serializers import GroupSerializer, PermissionSerializer, GroupWriteSerializer
from utils.permissions import GroupsIsOwnerOrReadOnly
from utils.filters import GroupFilter
from utils.pagination import Pagination
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class GroupsViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
            Create a model instance.
            Retrieve a model instance.
            List a model instance.
            update a model instance.
            delete a model instance.
    """
    queryset = Group.objects.all().order_by("-id")
    serializer_class = GroupSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticated, GroupsIsOwnerOrReadOnly, DjangoModelPermissions)
    filter_class = GroupFilter
    search_fields = ('name','permissions__name')
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)

    # dynamic get serializer class for model.
    def get_serializer_class(self):
        if self.action == "list":
            return GroupSerializer
        elif self.action == "create" or self.action == 'update':
            return GroupWriteSerializer
        return GroupSerializer


class PermissionViewSet(CacheResponseMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
            Create a model instance.
            Retrieve a model instance.
            List a model instance.
    """
    queryset = Permission.objects.all().order_by("-id")
    serializer_class = PermissionSerializer
    pagination_class = Pagination

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list" or self.action == "retrieve":
            return [IsAuthenticated(), ]
        elif self.action == "create":
            return [IsAdminUser(), ]
        return []
