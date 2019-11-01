from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('accounts:accounts_detail', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.username
