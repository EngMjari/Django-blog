from django.shortcuts import render


def homePage(request):
    template = "pages/index.html"
    context = {}
    return render(request, template, context)


def blogView(request):
    template = "pages/blog.html"
    context = {}
    return render(request, template, context)


def categoryView(request, slug="salam"):
    template = "pages/category.html"
    context = {
      "title": "slug",
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
