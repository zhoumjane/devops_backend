from .views import UserViewSet
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register("user", UserViewSet, basename="user")