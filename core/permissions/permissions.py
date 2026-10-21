from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class _RolePermission(BasePermission):
    role: str

    def has_permission(self, request: Request, view: APIView) -> bool:
        user = request.user
        if not (user and user.is_authenticated):
            return False
        return bool(user.is_superuser or getattr(user, "role", None) == self.role)


class IsStaffRole(_RolePermission):
    role = "staff"
    message = "Staff access required."


class IsMemberRole(_RolePermission):
    role = "member"
    message = "Member access required."
