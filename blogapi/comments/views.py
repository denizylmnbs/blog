from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('pk'),
            author=self.request.user)