from django.urls import path
from .views import PostCreate, PostList, PostRetrieveUpdateDestroy
from comments.views import CommentListCreateView
from likes.views import LikeListCreateView

urlpatterns = [
    path('create/', PostCreate.as_view(), name='post-create'),
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
    path('<int:pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),  # Include comment URLs for a specific post
    path('<int:pk>/likes/', LikeListCreateView.as_view(), name='like-list-create'),  # Include like URLs for a specific post
]