from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_id)