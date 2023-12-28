from django.shortcuts import render

def homePage(request):
  template = "pages/index.html"
  context = {
    
  }
  return render(request, template, context)