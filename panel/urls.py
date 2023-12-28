from django.urls import path
from .views import (
  panelView,
  createPostBlog
  
)
urlpatterns = [
    path('', panelView, name="panelView"),
    path("post/create", createPostBlog, name="CreatePost")
]
