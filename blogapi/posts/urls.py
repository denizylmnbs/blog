from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from comments.views import CommentListCreateView
from likes.views import LikeListCreateView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('<int:pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),  # Include comment URLs for a specific post
    path('<int:pk>/likes/', LikeListCreateView.as_view(), name='like-list-create'),  # Include like URLs for a specific post
] + router.urls