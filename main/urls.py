from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signup", views.signUp, name="signUp"),
    path("login", views.signIn, name="signIn"),
    path("signout", views.signOut, name="signOut"),
    path("dashboard", views.dashboard, name="dashboard"),

]
