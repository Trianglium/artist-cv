from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from about.models import Entry, Section

# Add a new entry to resume
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['resume_section', 'content']

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

# Add a new section (title) to Resume [EG 'Education', 'Volunteer Experience', 'Awards']
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))




class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=255, required=True)
    contact_email = forms.EmailField(required=True)
    contact_msg = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))




