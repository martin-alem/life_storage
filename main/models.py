from django.db import models
from authentication.models import User


class Media(models.Model):
    CATEGORY = [
        ("IMG", "IMAGE"),
        ("VID", "VIDEO"),
        ("AUD", "AUDIO"),
        ("FIL", "FILE")
    ]
    name = models.CharField(verbose_name="name", max_length=30, unique=True)
    size = models.IntegerField(verbose_name="size")
    description = models.TextField(verbose_name="description")
    type = models.CharField(verbose_name="type", max_length=20)
    downloads = models.IntegerField(verbose_name="downloads")
    media_url = models.CharField(verbose_name="media_url", max_length=255)
    category = models.CharField(verbose_name="category", max_length=100, choices=CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
