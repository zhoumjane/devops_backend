from rest_framework.routers import DefaultRouter
from .views import GroupsViewSet,PermissionViewSet

group_router = DefaultRouter()
group_router.register(r'groups', GroupsViewSet, basename="groups")
group_router.register(r'permissions', PermissionViewSet, basename="permissions")