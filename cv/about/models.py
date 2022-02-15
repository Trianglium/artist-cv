from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.models import User

# About Section Model; Customizable.
# Example About Sections: "Work Experience", "Education and Certification", "Technologies and Languages", "Skills", "Objective", etc.
class Section(models.Model):
    # subject as in, the way police talk about a person of interest.
    # synonyms for this field are "owner", "author", "me" (in "about me"), "person", etc.
    subject = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=155, null=True, editable=True)
    body = models.TextField(null=True, editable=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)





# TO DO - Integrate Custom Auth User Model into Contact Model
# Would be beneficial if the default for some of these these fields
# could be the required Auth User Model Fields
# Idea - Should Contact Model just have generic fields
# to let the user input their contact method and value?

class Contact(models.Model):
    email = models.EmailField(null=True, editable=True),
    number = models.IntegerField(null=True, editable=True)
    subject = models.CharField(max_length=255, null=True, editable=False)
    body = models.CharField(max_length=800, null=True, editable=False)


    def __str__(self):
        return self.subject

