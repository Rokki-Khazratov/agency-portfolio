from rest_framework import permissions

class IsAdminOr404(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        if request.user and request.user.is_staff:
            return True
        
        return False
