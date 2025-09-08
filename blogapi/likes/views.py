from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer

# Create your views here.

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('pk'),
            user=self.request.user)