from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from .utils import util
from authentication.models import User
from .models import Media


def home(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = Media.objects.filter(user=user)
        return render(request, "main/home.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def images(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="IMG", user=user)
        return render(request, "main/images.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def videos(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="VID", user=user)
        return render(request, "main/videos.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def audios(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="AUD", user=user)
        return render(request, "main/audios.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def files(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="FIL", user=user)
        return render(request, "main/files.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def upload(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        if request.method == "POST":
            name = request.POST["name"]
            size = request.POST["size"]
            description = request.POST["description"]
            media_type = request.POST["type"]
            downloads = 0
            media_url = request.POST["media_url"]
            category = request.POST["category"]
            user = user

            media = Media.objects.create(name=name, size=size, description=description, type=media_type, downloads=downloads, media_url=media_url, category=category, user=user)
            return render(request, "main/home.html", {"user": user, "medias": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def search(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        if request.method == "GET":
            query = request.GET['search']
            media = Media.objects.filter(name__icontains=query, user=user)
            return render(request, "main/search.html", {"user": user, "medias": media, "query":query})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def logout(request):
    if request.method == "GET":
        redirect_url = reverse("login")
        response = HttpResponseRedirect(redirect_url)
        response.delete_cookie(key="_access_token", path="/", domain=None, samesite="strict")
        return response
