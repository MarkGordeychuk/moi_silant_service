from rest_framework import permissions


class MachinePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)

        if request.method in permissions.SAFE_METHODS:
            return bool(user and user.is_authenticated)

        return super().has_permission(request, view)


class MaintenancePermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        user = getattr(request, 'user', None)
        is_auth = bool(user and user.is_authenticated)

        if request.method in permissions.SAFE_METHODS:
            return is_auth

        return is_auth and (
                    obj.client == user or obj.service_company == user or super().has_object_permission(request, view,
                                                                                                       obj))


class ComplaintPermission(permissions.DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        user = getattr(request, 'user', None)
        is_auth = bool(user and user.is_authenticated)

        if request.method in permissions.SAFE_METHODS:
            return is_auth

        return is_auth and (obj.service_company == user or super().has_object_permission(request, view, obj))
