from django.shortcuts import render
from django.http import HttpResponse
from .models import feature
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def index(request):
    features = feature.objects.all()
    return render(request, "index.html", {"features": features})


def counter(request):
    text = request.POST["text"]
    amount_of_words = len(text.split())
    return render(request, "render.html", {"result": amount_of_words})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already used mah homie")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "password not right kiddo")
            return redirect(register)
    else:
        return render(
            request,
            "register.html",
        )


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            authenticate(user)
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "login credentials not ok lol")
            return redirect("login")
    else:
        return render(
            request,
            "login.html",
        )


def user_logout(request):
    logout(request)
    return redirect("login")
