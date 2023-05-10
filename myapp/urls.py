from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
]
