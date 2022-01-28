from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="projects")

    def __str__(self):
        return self.title
