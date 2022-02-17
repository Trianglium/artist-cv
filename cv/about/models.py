from django.db import models
from django.conf import settings
from django.conf import settings
from django.contrib.auth.models import User




class Category(models.Model):
    title = models.TextField(
        max_length = 100,
        unique = True,
        help_text = "Elements (or Element titles) are the Titles of Resume Sections. \nIE 'Education', 'Experience', 'Objective', and etc. \nNew Sections can be entered here if the one you'd like to include, does not already exist. \nTIP: You can check to see if it exists by creating a new Resume Section object"
        )

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title.upper()



# About Section Model; Customizable.
# Example About Sections: "Work Experience", "Education and Certification", "Technologies and Languages", "Skills", "Objective", etc.
class Resume(models.Model):
    section = models.ManyToManyField(Category, related_name="me")

    title = models.CharField(max_length=55, null=True, editable=True)
    head = models.CharField(max_length=75, null=True, editable=True)
    summary = models.TextField(max_length=500, null=True, editable=True)

    start = models.DateField(null=True, editable=True)
    end = models.DateField(null=True, editable=True)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'[{self.section_subject}] | {self.title}'
