import hashlib

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .utils import validate


def login(request):
    return render(request, "authentication/login.html")


def registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        # perform server side validation and sanitization
        if not validate.validate_name(first_name) or not validate.validate_name(last_name) or not validate.validate_email(email) or not validate.validate_password(password):
            return render(request, "authentication/registration.html", {
                "error": "One or more fields is invalid. Check and try again",
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

        # check to make sure another user does not exist with same email
        users = User.objects.filter(email=email)
        if len(users) > 0:
            return render(request, "authentication/registration.html", {
                "error": "A user already exist with the email",
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

        # persist new user to database
        try:
            # hash the user password
            password = hashlib.sha224(bytes(password, "utf8")).hexdigest()
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            user_token = new_user.id
            redirect_url = reverse("login")
            salt = "90bed65b7fb6e1129b4de3309c7c1938b6274744cc8a7527a6"
            response = HttpResponseRedirect(redirect_url)
            response.set_signed_cookie(key="_user_token", value=user_token, salt=salt, max_age=60, expires=None, path="/", domain=None, secure=False, httponly=True, samesite="Strict")
            return response
        except IntegrityError:
            return render(request, "authentication/registration.html", {
                "error": "Unable to create an account. Please try again later.",
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

    return render(request, "authentication/registration.html", {
        "error": None,
    })
