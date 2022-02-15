from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile

from projects.humanize import naturalsize
from projects.models import Project, Content, Link
from taggit.forms import TagField



# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    content_upload = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'content_upload'

    class Meta:
        model = Project
        fields = ['title', 'summary', 'description', 'content_upload', 'skills']

    # Validate the size of the content
    def clean(self):
        cleaned_data = super().clean()
        pc_media = cleaned_data.get('content_upload')
        if pc_media is None:
            return
        if len(pc_media) > self.max_upload_limit:
            self.add_error('content_upload', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust media if it is a freshly uploaded file
        f = instance.content_upload   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            project_content = Content(media=bytearr, content_type=f.content_type)
            project_content.save()
            instance.content_upload = project_content
            # Overwrite with the actual media data

        if commit:
            instance.content_upload.add(project_content)
            instance.save()
            self.save_m2m()


        return instance
