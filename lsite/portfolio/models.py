from django.db import models
from django.conf import settings

class Category(models.Model):
    PROJECT_TYPES = (
        ('AVT', 'Audio Visual Technology'),
        ('VA', 'Visual Art')
    )
    name = models.CharField(
        max_length=3,
        choices=PROJECT_TYPES,
         help_text = "Choose AVT for Sound, Music, Video, Editing and etc. Choose Visual Art for Non-Video / Sound Graphic Designs, Drawings, Paintings and etc."
    )


    def __str__(self):
        return self.name

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class Project(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="projects")

    def __str__(self):
        return self.title
