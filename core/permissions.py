from rest_framework import permissions


def is_in_group_factory(allowed_groups):
    class IsInGroup(permissions.BasePermission):
        def has_permission(self, request, view):
            user_groups = request.user.groups.values_list("name", flat=True)
            return any(group in user_groups for group in allowed_groups)

    return IsInGroup
