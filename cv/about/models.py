from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField



# Resume Section - EG, 'Experience', 'Skills', 'Education', 'Awards', etc
class Section(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Generic ActiveDates Model gives the ability to add dates to resume section content, where it is relavent.
# While also being able to not add dates to every single section entry
class ActiveDate(models.Model):
    start_date = models.TextField(null=True, blank=True)
    end_date = models.TextField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


# Main Body of Content to put within the resume section - EG, under 'Skills' one might enter 'Django'
class Entry(models.Model):
    content = RichTextField(blank=True, null=True)
    resume_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    dates = GenericRelation(ActiveDate)

