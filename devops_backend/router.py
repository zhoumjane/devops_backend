from rest_framework.routers import DefaultRouter
from users.urls import user_router
from groups.urls import group_router
from servers.urls import server_router
from images.urls import image_router

route = DefaultRouter()
route.registry.extend(user_router.registry)
route.registry.extend(group_router.registry)
route.registry.extend(server_router.registry)
route.registry.extend(image_router.registry)