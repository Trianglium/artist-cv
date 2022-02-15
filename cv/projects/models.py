from django.db import models
from django.core.validators import MinLengthValidator, URLValidator
from django.conf import settings

from taggit.managers import TaggableManager


class Project(models.Model):
    # Title of the Project, give it a unique name.
    title = models.CharField(
        max_length=200,
        unique=True,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    # Use Summary as a preview for your post.
    # People viewing your site will see the summary before they decide whether or not to view the Project details.
    # Similar to what you see on a google results page before deciding to click on a website result.
    summary = models.CharField(max_length=155)
    # Description of the project (in depth, or not, use as you please).
    # This is where you describe the actual  details of everything.
    # There is no set max length for the description field.
    description = models.TextField()
    # Use the skill field as a sort of ‘tag’ for what the project is about.
    # It’s recommended that skill names remain consistent as to help with navigating the site.
    skills = TaggableManager(blank=True)
    # Owner & Technical Info
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Shows up in the admin list
    def __str__(self):
        return self.title

# Project Link (URL) - for External Content that needs to be included
class Link(models.Model):
    name = models.CharField(max_length=255, help_text='Name your URL something meaningful. This field is public.', editable=True)
    info = models.TextField(help_text='Add a Short Description for this URL. This field is public.', null=True, editable=True)
    url = models.URLField(
        max_length=1000,
        unique=True,
        editable=True,
        validators=[URLValidator(message='Enter a valid URL - must be unqiue.')]
    )
    # https://anonfiles.com/1eB4O6H0x0/Orchestral_Intro_17_April_2021_mp3
    # Media - Add URL to your external content file (Optional)
    projects = models.ManyToManyField(Project, editable=True, help_text='Copy and Paste the url to the external content you want to include')

    def __str__(self):
        return self.name

class Content(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Uploads for Project. Any Images, Files, or ETC thats to be used with a Project Post.
    project_content = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    # Media - Upload to MemoryStorage (Optional)
    projects = models.ManyToManyField(Project, editable=True, help_text='Upload the Content to use with this project post and to store in memory.')

    def __str__(self):
        return self.name


