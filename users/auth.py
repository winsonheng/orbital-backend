from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Ensure AUTHENTICATION_BACKENDS in settings.py points to this class

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None