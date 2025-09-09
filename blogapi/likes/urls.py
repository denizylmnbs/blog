from django.urls import path, include
from .views import LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LikeViewSet, basename='like')

urlpatterns = [

] + router.urls