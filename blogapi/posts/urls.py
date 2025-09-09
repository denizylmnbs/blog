from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('<int:pk>/comments/', include('comments.urls')),  # Include comment URLs for a specific post
    path('<int:pk>/likes/', include('likes.urls')),  # Include like URLs for a specific post
] + router.urls