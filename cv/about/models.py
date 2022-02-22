from django.db import models
from ckeditor.fields import RichTextField

class Section(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Entry(models.Model):
    content = RichTextField(blank=True, null=True)
    resume_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    start_date = models.TextField(null=True, blank=True)
    end_date = models.TextField(null=True, blank=True)