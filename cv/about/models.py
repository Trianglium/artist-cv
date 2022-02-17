from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.models import User




class Subject(models.Model):
    name = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.value



# About Section Model; Customizable.
# Example About Sections: "Work Experience", "Education and Certification", "Technologies and Languages", "Skills", "Objective", etc.
class CustomSection(models.Model):
    head = models.CharField(max_length=155, null=True, editable=True)
    body = models.TextField(max_length=2000, null=True, editable=True)
    section_subject = models.ManyToManyField(Subject, related_name="sections")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}] | {} '.format(self.section_subject, self.head)
