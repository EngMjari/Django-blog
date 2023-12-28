from django.shortcuts import render



def panelView(request):
  template = 'admin/adminPanel.html'
  context = {
    
  }
  return render(request, template, context)


def createPostBlog(request):
  template = 'admin/createPostBlog.html'
  context = {
    
  }
  return render(request, template, context)


