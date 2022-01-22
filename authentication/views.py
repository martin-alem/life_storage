from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .utils import validate, util


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        context = {"error": None}

        # hash the password
        password = util.hash_password(password)

        # attempt to find the user
        try:
            user = User.objects.get(email=email, password=password)
            user_token = user.id
            redirect_url = reverse("home")
            response = HttpResponseRedirect(redirect_url)
            util.set_cookie("_access_token", user_token, response)
            return response
        except User.DoesNotExist:
            context["error"] = "Invalid Email or Password"
            return render(request, "authentication/login.html", context)

    return render(request, "authentication/login.html")


def registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        context = {
            "error": None,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }

        # perform server side validation and sanitization
        if not validate.validate_name(first_name) or not validate.validate_name(last_name) or not validate.validate_email(email) or not validate.validate_password(password):
            context["error"] = "One or more fields is invalid. Check and try again"
            return render(request, "authentication/registration.html", context)

        # check to make sure another user does not exist with same email
        users = User.objects.filter(email=email)
        if len(users) > 0:
            context["error"] = "A user already exist with the email"
            return render(request, "authentication/registration.html", context)

        # persist new user to database
        try:
            # hash the user password
            password = util.hash_password(password)
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            user_token = new_user.id
            redirect_url = reverse("home")
            response = HttpResponseRedirect(redirect_url)
            util.set_cookie("_access_token", user_token, response)
            return response
        except IntegrityError:
            context["error"] = "Unable to create an account at the moment. Try again later"
            return render(request, "authentication/registration.html", context)

    return render(request, "authentication/registration.html", {"error": None})
