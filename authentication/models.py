from django.db import models


class User(models.Model):
    first_name = models.CharField(verbose_name="first_name", max_length=20)
    last_name = models.CharField(verbose_name="last_name", max_length=20)
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    password = models.CharField(verbose_name="password", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")


class Media(models.Model):
    CATEGORY = [
        ("IMG", "IMAGE"),
        ("VID", "VIDEO"),
        ("AUD", "AUDIO"),
        ("FIL", "FILE")
    ]
    name = models.CharField(verbose_name="name", max_length=30, unique=True)
    size = models.IntegerField(verbose_name="size")
    type = models.CharField(verbose_name="type", max_length=20)
    downloads = models.IntegerField(verbose_name="downloads")
    media_url = models.CharField(verbose_name="media_url", max_length=255)
    category = models.CharField(verbose_name="category", max_length=100, choices=CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
