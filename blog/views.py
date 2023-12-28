from django.shortcuts import render, get_object_or_404
from .models import Category

def homePage(request):
    template = "pages/index.html"
    context = {}
    return render(request, template, context)


def blogView(request):
    template = "pages/blog.html"
    context = {}
    return render(request, template, context)


def categoryView(request, slug="all"):
    if slug == "all" : 
      model = Category.objects.all()
    else:
      model = get_object_or_404(Category.objects.filter(slug=slug))
    template = "pages/category.html"
    context = {
      "title": slug,
    }
    return render(request, template, context)


def LoginView(request):
    template = "pages/login.html"
    context = {}
    return render(request, template, context)


def registerView(request):
    template = "pages/register.html"
    context = {}
    return render(request, template, context)
