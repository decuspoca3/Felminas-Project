from django.db import models
from django.contrib.auth.models import User

from .models import Register

class RegisterManager(models.Manager):
    def get(self, username):
        """
        Get the `Register` object with the given username.

        Args:
            username: The username of the `Register` object to get.

        Returns:
            The `Register` object with the given username.
        """

        return self.filter(username=username).get()

