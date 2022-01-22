from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout, name="logout"),
    path("images", views.images, name="image"),
    path("videos", views.videos, name="video"),
    path("audios", views.audios, name="audio"),
    path("files", views.files, name="file"),
    path("upload", views.upload, name="upload"),
    path("search", views.search, name="search")
]
