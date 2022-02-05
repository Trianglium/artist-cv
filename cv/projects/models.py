from django.db import models

class Project(models.Model):
    # Title of the Project, give it a unique name.
    title = models.CharField(max_length=100, unique=True)
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
    skill = models.CharField(max_length=20)
    # Optional Image of or for Project
    image = models.FilePathField(path="/media/img", null=True)
    # Optional Audio / Sound for or of Project
    # Intended for Musicians and Sound Related Artistis
    sound = models.FilePathField(path="/media/audio", null=True)
    # Optional video / clip for or of  project
    video = models.FilePathField(path="/media/vid", null=True)
