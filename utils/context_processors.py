from blog.models import Category

def category_context(request):
  model = Category.objects.all()[:5]
  return {
    'navbar_category': model
  }