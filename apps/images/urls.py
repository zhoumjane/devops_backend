from .views import ImageViewSet
from rest_framework.routers import DefaultRouter

image_router = DefaultRouter()
image_router.register("images", ImageViewSet, basename='images')
