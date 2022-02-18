from django.db import models
from django.conf import settings
from django.core.validators import URLValidator


class BaseAutoDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
       abstract = True

class BaseContent(BaseAutoDate):
    content = models.TextField()

    class Meta:
       abstract = True

class BaseArticle(BaseContent):
    title = models.TextField(max_length=200)
    summary = models.TextField(max_length=155)

    class Meta:
       abstract = True

class BaseLink(models.Model):
    label = models.CharField(max_length=50, help_text='Website Name', null=True, editable=True)
    url = models.URLField(
        max_length=1000,
        unique=True,
        editable=True,
        validators=[URLValidator(message='Enter a valid (unqiue) URL')]
    )

    class Meta:
       abstract = True



class Organization(models.Model):
    # Name of the Company, Employer, School, Charity, Camp, Website, or Entity, (ETC) who either employed, or educated, you
    institution = models.CharField(max_length=155, null=True, editable=True, help_text='Name of the Company, Organization, University, Website, Institution, Chairty, Establishment (and or etc)')
    # Month / Year of first day (Day can be set to whatever, it will be ignored)
    start_date = models.DateTimeField(auto_now=True, help_text='Input Month / Year of first day (Day can be set to whatever, it will be ignored')
    # Month / Year of last day (Day can be set to whatever, it will be ignored)
    end_date = models.DateTimeField(auto_now=True, help_text='Input Month / Year of last day (Day can be set to whatever, it will be ignored')
    # Basic summary. What you did there (if work). Made for "Jobs" but can be added to any model.
    overview = models.TextField(null=True, editable=True, help_text='Basic Summary of what you did there')
    # Achievements and other notable details to highlight/emphasize
    highlights = models.TextField(null=True, editable=True, help_text='Achievements, awards, and other notable details to highlight/emphasize')
    # (Optional) Meant for professional fields (IE Job and etc) or Institutions where location is relavent.
    location = models.TextField(null = True, editable=True, help_text='(Optional) Meant for professional fields (IE Job and etc) or Institutions where location is relavent.')


    class Meta:
        abstract = True

class Skill(models.Model):
    # Label for the skill. IE "Python Programming", "Interpretive Dance", "Microsoft Office"
    skill_name = models.CharField(max_length=155, null=True, editable=True, help_text="What do you call this skill? What do you type in to google, to find information about this skill?")
    # Choices for proficiency level
    LEVEL_CHOICES = [
        ('N', 'Novice'), # New Beginner
        ('C', 'Competent'), # Beginner transitioning to Intermediate
        ('P', 'Proficient'), # Intermediate to Advanced
        ('E', 'Expert'), # Advanced to Mastery
    ]
    proficiency_level = models.CharField(
        max_length=1,
        choices=LEVEL_CHOICES,
        default='P',
        help_text="(Private Field Only) The Input from this field is used to sort your skills by how comfortable you are, interviewing in them. No one will know what level you enter, other than you. Skills will be sorted, most proficient to least proficient as to emphasize the skills that you are the best at.\nNovice = Beginner, \nCompetent = Beginner to Intermediate, \nProficient = Intermediate to Advanced, \nExpert = Advanced to Mastery",
    )
    class Meta:
        abstract = True












