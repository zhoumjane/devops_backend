from .serializers import ServerSerializer
from .models import Server
from utils.permissions import ServersIsOwnerOrReadOnly
from rest_framework import viewsets, filters, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from utils.pagination import Pagination
from utils.filters import ServersFilter
from django_filters.rest_framework import DjangoFilterBackend


class ServerViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
        Create a model instance.
        Retrieve a model instance.
        List a model instance.
        update a model instance.
        delete a model instance.
    """
    queryset = Server.objects.all().order_by("-id")
    serializer_class = ServerSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticated, ServersIsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ServersFilter
    search_fields = ('hostname', 'ip', 'status', 'remark', 'project', 'asset', 'owner__username', 'server_type')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PermissionCheck(viewsets.ViewSet, mixins.ListModelMixin):
    """
        permission check.
    """

    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):

        ip_addr = self.request.query_params['ip']
        permission_str = 'servers.login_' + ip_addr
        if not (self.request.user.has_perm('servers.login_server') or self.request.user.has_perm(permission_str)):
            return Response({"permission": False}, status=status.HTTP_403_FORBIDDEN)
        try:
            Server.objects.get(ip=ip_addr)
        except Exception as e:
            return Response({"permission": False}, status=status.HTTP_400_BAD_REQUEST)
        data = {"permisson": True}
        return Response(data, status=status.HTTP_200_OK)
