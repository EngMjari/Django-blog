from django.urls import path
from .views import (
    homePage, 
    blogView,
    categoryView,

)
urlpatterns = [
    path("", homePage, name="Homepage"),
    path("blog/", blogView, name="blogPage"),
    path("category/<slug:slug>/", categoryView, name="categoryPage"),
]
