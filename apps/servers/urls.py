from .views import ServerViewSet, PermissionCheck
from rest_framework.routers import DefaultRouter

server_router = DefaultRouter()
server_router.register("servers", ServerViewSet, basename='servers')
server_router.register('permission_check', PermissionCheck, basename='permission_check')
