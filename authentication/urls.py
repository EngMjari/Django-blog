from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
  registerView,
  logoutView,
)
urlpatterns = [
    path("register", registerView, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', logoutView , name='logout'),
]