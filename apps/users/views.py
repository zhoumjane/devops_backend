from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserWriteSerializer
from utils.permissions import UsersIsOwnerOrReadOnly
from utils.pagination import Pagination
from utils.filters import UsersFilter
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class UserViewSet(CacheResponseMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticated, UsersIsOwnerOrReadOnly, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'email', 'groups__name')

    def get_serializer_class(self):
        if self.action == "list":
            return UserSerializer
        elif self.action == "create" or self.action == 'update' or self.action == 'partial_update':
            return UserWriteSerializer
        return UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
