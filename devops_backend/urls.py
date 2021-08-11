"""devops_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include,re_path
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from utils.sso_auth.views import obtain_jwt_token as sso_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from devops_backend import settings
from .router import route
from apps.sshchan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('docs/', include_docs_urls("自动化平台")),
    path('api-auth/', include("rest_framework.urls", namespace='rest_framework')),
    path('api-auth-token/', sso_jwt_token),
    path('webssh/', views.index),
    path('upload_ssh_key/', views.upload_ssh_key),
    re_path('^media/(?P<path>.*)$', serve, {"document_root":settings.MEDIA_ROOT})
]