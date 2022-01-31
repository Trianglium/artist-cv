from django.db import models
from django.conf import settings

# Categorize the type of Art Project
# Category name choices influenced by Britannica;
# https://www.britannica.com/topic/the-arts

class Category(models.Model):
    PROJECT_TYPES = (
        ('L', 'Literature'),
        ('VA', 'Visual Arts'),
        ('GA', 'Graphic Arts'),
        ('PLA', 'Plastic Arts'),
        ('DA', 'Decorative Arts'),
        ('PFA', 'Performing Arts'),
        ('M', 'Music'),
        ('ARC', 'Architecture')
    )
    name = models.CharField(
        max_length=3,
        choices=PROJECT_TYPES,
         help_text = """
         <i>This is a general guide, feel free to use the categories however you wish.</i>
         <br> The Categories will be used to split up portfolio sections based on art type.
         <br>
         <br>Explanation of the Named Categories:<br>
            <br>(Literature) = including poetry, drama, story, and so on.
            <br>(Visual Arts) = painting, drawing, sculpture, etc.
            <br>(Graphic Arts) = painting, drawing, design, and other forms expressed on flat surfaces.
            <br>(Plastic Arts) = sculpture, modeling, etc.
            <br>(Decorative Arts) = enamelwork, furniture design, mosaic, etc.
            <br>(Performing Arts) = theatre, dance, music.
            <br>(Music) = composition, sound, and so on.
            <br>(Architecture) = includes interior design.
            <br>
            <br><i>If a category doesn't quite feel right, choose the closet category and add the more suitable category name as a tag.</i>
         """
    )


    def __str__(self):
        return self.name

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class Project(models.Model):
    # Name of Project / Project title.
    title = models.TextField(max_length=100)
    # Slug is an automatic field.
    slug = models.SlugField()
    # Summary to show as a preview. Not the full text.
    summary = models.TextField(max_length=500)

    # Image file. Optional field.
    media = models.ImageField(upload_to='images', null=True, editable=True)

    # URL Field for Audio
    link = models.URLField(null=True, editable=True)

    # Longer / Full Summary. Talk about your project in this field.
    content = models.TextField()
    # Art Category of Project (Categories will be split into different portfolio pages)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Additional tags for the project (This will help with search and more.)
    tags = models.ManyToManyField(Tag, related_name="projects")

    def __str__(self):
        return self.title
