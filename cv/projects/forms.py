from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile

from projects.humanize import naturalsize
from projects.models import Project, Content, Link
from taggit.forms import TagField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create the mediaform class.
class MediaForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    media = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'media'

    class Meta:
        model = Content
        fields = ['name', 'media']

    # Validate the size of the content
    def clean(self):
        cleaned_data = super().clean()
        pc_media = cleaned_data.get('media')
        if pc_media is None:
            return
        if len(pc_media) > self.max_upload_limit:
            self.add_error('media', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object
    def save(self, commit=True):
        instance = super(MediaForm, self).save(commit=False)

        # We only need to adjust media if it is a freshly uploaded file
        f = instance.media
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.media = bytearr

        if commit:
            instance.save()
            self.save_m2m()



        return instance



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        #fields = ['title', 'summary', 'description', 'content_upload', 'skills']
        fields = "__all__"
        exclude = ['created_at', 'modified_at']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
