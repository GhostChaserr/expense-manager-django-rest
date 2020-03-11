from django.contrib.auth.backends import ModelBackend
from .models import User

class Backend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.ObjectDoesNotExist:
            return None