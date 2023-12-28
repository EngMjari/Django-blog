from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="post-image/")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
