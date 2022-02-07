from django.db import models
from django.core.validators import MinLengthValidator
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
    skill = TaggableManager(blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Media
    project_content = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title
