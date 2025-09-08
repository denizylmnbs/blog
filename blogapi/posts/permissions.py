from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    message = "You must be the author of this post to edit or delete it."

    def has_object_permission(self, request, view, obj):
        # GET/HEAD/OPTIONS serbest; yazma işlemleri sadece yazara
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, "author_id", None) == getattr(request.user, "id", None)