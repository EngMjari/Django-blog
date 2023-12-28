from django.urls import path
from .views import (
    homePage, 
    blogView,
    categoryView,
    LoginView,
    registerView,
)
urlpatterns = [
    path("", homePage, name="Homepage"),
    path("blog/", blogView, name="blogPage"),
    path("category/<slug:slug>/", categoryView, name="categoryPage"),
    path("login/", LoginView, name="loginPage"),
    path("register/", registerView, name="registerPage"),
]
