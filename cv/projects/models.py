from django.db import models
from django.conf import settings

from taggit.managers import TaggableManager
from base.models import BaseArticle, BaseLink



class Content(models.Model):
    # Uploads for Project. Any Images, Files, or ETC thats to be used with a Project Post.
    media = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    name = models.CharField(max_length=100, blank=True)
    # Media - Upload to MemoryStorage (Optional)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.content_type


# Project Link (URL) - for External Content that needs to be included
class Link(BaseLink):
    alt = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        editable=True,
        help_text='(Optional) Add a Short Description for this URL. This field is public.',
    )

    # https://anonfiles.com/1eB4O6H0x0/Orchestral_Intro_17_April_2021_mp3
    # Media - Add URL to your external content file (Optional)

    def __str__(self):
        if self.label:
            return self.label
        else:
            return self.url

class Project(BaseArticle):
    # Inherits all fields from BaseArticle
    # NOTE: the 'content' field was once called 'description'

    # Media - Upload to MemoryStorage (Optional)
    content_upload = models.ManyToManyField(
        Content,
        related_name='project_content',
        blank=True,
        editable=True,
        help_text='Upload the Content to use with this project post and to store in memory. \nUploading media content does not work through the administration panel.',
    )

    # Link - External Media Resource or Other URL to include
    links = models.ManyToManyField(
        Link,
        blank=True,
        editable=True,
        related_name='projects',
        help_text='Copy and Paste the url to the external content you want to include',
    )
    # Use the skill field as a sort of ‘tag’ for what the project is about.
    # It’s recommended that skill names remain consistent as to help with navigating the site.
    skills = TaggableManager(blank=True)
    # Owner & Technical Info
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_owner')


    # Shows up in the admin list
    def __str__(self):
        return self.title

