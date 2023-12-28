from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(
        max_length=20,
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        print(slugify(self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


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

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
