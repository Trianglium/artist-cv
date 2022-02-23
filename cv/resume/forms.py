from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from resume.models import Professional, Educational, Volunteer, Technical, Interpersonal, ProfessionalProfile

class JobForm(forms.ModelForm):
    class Meta:
        model = Professional
        exclude = ['created_at', 'modified_at']

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class EducationalForm(forms.ModelForm):
    class Meta:
        model = Professional
        exclude = ['created_at', 'modified_at']

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Professional
        exclude = ['created_at', 'modified_at']

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))