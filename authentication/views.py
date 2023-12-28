from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def LoginView(request):
    template = "auth/login.html"
    context = {}
    return render(request, template, context)


def registerView(request):
    template = "auth/register.html"
    context = {}
    return render(request, template, context)


@login_required
def logoutView(request):
    logout(request)
    return redirect('/')