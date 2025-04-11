# program/context_processors.py
from .models import UserRole

def user_roles(request):
    if request.user.is_authenticated:
        try:
            role = request.user.userrole.role
        except UserRole.DoesNotExist:
            role = None
        return {
            'user_role': role,
            'is_admin': request.user.is_superuser
        }
    return {}
