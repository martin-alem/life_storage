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
        media = Media.objects.all()
        return render(request, "main/home.html", {"user": user, "media": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def images(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="IMG")
        return render(request, "main/images.html", {"user": user, "media": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def videos(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="VID")
        return render(request, "main/videos.html", {"user": user, "media": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def audios(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="AUD")
        return render(request, "main/audios.html", {"user": user, "media": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def files(request):
    logged_in = util.is_logged_in(request)
    if logged_in:
        user = User.objects.get(id=logged_in)
        media = util.fetch_all(Media, category="FIL")
        return render(request, "main/files.html", {"user": user, "media": media})

    redirect_url = reverse("login")
    return HttpResponseRedirect(redirect_url)


def logout(request):
    if request.method == "GET":
        redirect_url = reverse("login")
        response = HttpResponseRedirect(redirect_url)
        response.delete_cookie(key="_access_token", path="/", domain=None, samesite="strict")
        return response
