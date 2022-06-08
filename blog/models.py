from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Category Name")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField("Title", max_length=100)
    image = models.ImageField("Image", upload_to="media/")
    summary = models.CharField("Summary", max_length=255)
    content = models.CharField("Content", max_length=100)
    is_published = models.BooleanField(default=True, verbose_name="Published")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name="Category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="author")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("-time_create", )