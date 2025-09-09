from rest_framework import viewsets, permissions
from .models import Like
from .serializers import LikeSerializer

# Create your views here.

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.filter()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Like.objects.filter(post_id=post_id)