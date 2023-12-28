from django.contrib import admin
from .models import (
  Category, BlogPost
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('date_created', 'author', 'title', 'context', 'is_published', 'date_published', 'image')