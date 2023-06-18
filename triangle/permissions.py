from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

class IsAdminOrReadOnlyAndCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        
        return bool(request.user and request.user.is_staff)

class IsAdminOrAuthenticatedCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        print()
        print(request.user)
        print()
       
        
        #! ЧОмусь не працює. В в request.user не словник, а рядок
        # if request.user.auth and request.method=='POST':
        #     return True

        return bool(request.user and request.user.is_staff)

