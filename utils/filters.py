import django_filters
from servers.models import Server
from images.models import Image
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import Group

User = get_user_model()


class ServersFilter(django_filters.rest_framework.FilterSet):
    """
        Server filtering class.
    """
    hostname = django_filters.CharFilter(field_name="hostname",lookup_expr='icontains', label=u'主机名')
    server_type = django_filters.CharFilter(field_name="server_type", lookup_expr='icontains', label=u'服务器类型')
    ip = django_filters.CharFilter(field_name="ip",lookup_expr='icontains', label=u'IP地址')
    status = django_filters.CharFilter(field_name="status",lookup_expr='icontains', label='状态')
    last_time = django_filters.DateTimeFromToRangeFilter(field_name="last_time", lookup_expr='gte',label='到期时间')

    class Meta:
        model = Server
        fields = ["hostname", "ip", "status", "last_time", "server_type"]


class ImagesFilter(django_filters.rest_framework.FilterSet):
    """
        Image filtering class.
    """
    commit_id = django_filters.CharFilter(field_name="commit_id",lookup_expr='icontains')
    image_name = django_filters.CharFilter(field_name="image_name",lookup_expr='icontains')
    owner = django_filters.CharFilter(field_name="owner",lookup_expr='icontains')
    commit_time = django_filters.DateTimeFromToRangeFilter(field_name="commit_time", lookup_expr='gte')

    class Meta:
        model = Image
        fields = ["commit_id", "image_name", "owner", "commit_time"]


class UsersFilter(django_filters.rest_framework.FilterSet):
    """
        User filtering class.
    """
    username = django_filters.CharFilter(field_name="username", method="search_username")

    @classmethod
    def search_username(cls, queryset, name, value):
        print(name)
        return queryset.filter(Q(username__icontains=value) | Q(email__icontains=value))

    class Meta:
        model = User
        fields = ["username"]


class GroupFilter(django_filters.rest_framework.FilterSet):
    """
        User group filtering class.
    """

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = ['name']
