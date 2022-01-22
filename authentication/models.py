from django.db import models


class User(models.Model):
    first_name = models.CharField(verbose_name="first_name", max_length=20)
    last_name = models.CharField(verbose_name="last_name", max_length=20)
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    password = models.CharField(verbose_name="password", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")