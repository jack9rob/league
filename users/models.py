from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.get_full_name()}'
