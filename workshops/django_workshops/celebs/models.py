from django.db import models
from faker import Faker

class Celeb(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(first_name=f.first_name(), last_name=f.last_name())



