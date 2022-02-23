from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from about.models import Entry, Section

# Add a new entry to resume
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['resume_section', 'content', 'start_date', 'end_date']

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

