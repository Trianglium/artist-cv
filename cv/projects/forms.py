from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile

from projects.humanize import naturalsize
from projects.models import Project, Content
from taggit.forms import TagField



# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    project_content = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'project_content'

    class Meta:
        model = Content
        fields = ['project_content']

    # Validate the size of the project_content
    def clean(self):
        cleaned_data = super().clean()
        pc_media = cleaned_data.get('project_content')
        if pc_media is None:
            return
        if len(pc_media) > self.max_upload_limit:
            self.add_error('project_content', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust media if it is a freshly uploaded file
        f = instance.project_content   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.project_content = bytearr  # Overwrite with the actual media data

        if commit:
            instance.save()
            instance.project_set.create(uploads=instance)
            self.save_m2m()


        return instance
