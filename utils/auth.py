from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from devops_backend.settings import DOMAIN

User = get_user_model()


class CustomBackend(ModelBackend):
    """
        Custom user authentication
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            return user
        except ObjectDoesNotExist:
            email = username + DOMAIN
            user = User.objects.create(username=username, email=email)
            return user
        except Exception as e:
            return e