from rest_framework.permissions import DjangoObjectPermissions, BasePermission
from rest_framework import permissions


class GroupsIsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user in obj.owner.all():
            return True
        else:
            return False


class UsersIsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            if request.user.is_superuser:
                return True
            else:
                return False
        if request.user.is_superuser:
            return True
        return obj == request.user


class ServersIsOwnerOrReadOnly(DjangoObjectPermissions):

    def has_object_permission(self, request, view, obj):

        queryset = self._queryset(view)

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user in obj.owner.all():
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return request.user.has_perms(perms)

