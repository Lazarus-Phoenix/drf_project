from rest_framework import permissions

class IsModer(permissions.BasePermission):
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модераторы").exists()


class IsAdmin(permissions.BasePermission):
    message = "Вы не являетесь администратором"

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwner(permissions.BasePermission):
    message = "Вы не являетесь владельцем запрашиваемого объекта"

    def has_permission(self, request, view,obj):
        return obj.owner == request.user
