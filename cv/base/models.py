from django.db import models
from django.conf import settings
from django.core.validators import URLValidator


class BaseAutoDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
       abstract = True

class BaseContent(BaseAutoDate):
    content = models.TextField(null=True, blank=True, help_text='Input the main body of text (aka the main content)')

    class Meta:
       abstract = True

class BaseArticle(BaseContent):
    title = models.CharField(max_length=200, help_text='Title for this contentto be used as the headline')
    summary = models.CharField(max_length=155, help_text='Add a brief summary to show as a preview of the main content')

    class Meta:
       abstract = True

class BaseLink(models.Model):
    label = models.CharField(max_length=50, null=True, editable=True, help_text='Website Name or other label for this link. IE "LinkedIn", "Soundcloud", etc.')
    url = models.URLField(
        max_length=1500,
        unique=True,
        editable=True,
        validators=[URLValidator(message='Enter a valid (unqiue) URL')],
        help_text='Enter the URL for the link',
    )

    class Meta:
       abstract = True


class Organization(models.Model):
    # Name of the Company, Employer, School, Charity, Camp, Website, or Entity, (ETC) who either employed, or educated, you
    institution_name = models.CharField(max_length=155, null=True, editable=True, help_text='Name of the Company, Organization, University, School, Buisness, Website, Institution, Chairty, Establishment, etc.')
    # Month / Year of first day (Day can be set to whatever, it will be ignored)
    start_date = models.DateField(help_text='Input Month / Year of first day (Day can be set to whatever, it will be ignored')
    # Month / Year of last day (Day can be set to whatever, it will be ignored)
    end_date = models.DateField(help_text='Input Month / Year of last day (Day can be set to whatever, it will be ignored')
    # Basic summary. What you did there (if work). Made for "Jobs" but can be added to any model.
    overview = models.TextField(null=True, editable=True, help_text='Basic Summary of what you did there')
    # Achievements and other notable details to highlight/emphasize
    highlights = models.TextField(null=True, editable=True, help_text='Achievements, awards, and other notable details to highlight/emphasize')
    # (Optional) Meant for professional fields (IE Job and etc) or Institutions where location is relavent.
    location = models.CharField(
        max_length=200,
        null = True,
        blank=True,
        editable=True,
        help_text='(Optional) Meant for professional fields (IE Job and etc) or Institutions where location is relavent. Typically, Location is not relavent and this field can be left blank.',
    )

    def active_dates(self):
        self.start_date


    class Meta:
        abstract = True

class Skill(models.Model):
    # Label for the skill. IE "Python Programming", "Interpretive Dance", "Microsoft Office"
    skill_name = models.CharField(max_length=155, null=True, editable=True, help_text='Label / Name of the skill. IE "Critical Thinking", "Microsoft Office", "Django", "Leadership", etc. ')
    # Choices for proficiency level
    LEVEL_CHOICES = [
        ('N', 'Novice'), # New Beginner
        ('B', 'Advanced Beginner'),
        ('C', 'Competent'), # Beginner transitioning to Intermediate
        ('P', 'Proficient'), # Intermediate to Advanced
        ('E', 'Expert'), # Advanced to Mastery
    ]
    proficiency_level = models.CharField(
        max_length=1,
        choices=LEVEL_CHOICES,
        default='C',
        help_text='''(Private Field Only) The Input from this field is used to sort your skills on your resume related pages. The names of each level-choice option will not be featured publically.
        \nNo one will know what level a skill was set at, other than the person who entered it (you).
        \nSkills will be ordered by most proficient to least proficient as to emphasize the skills that you are the most confident about.
        \nNovice is the most beginner level while Expert level represents Mastery.
        \nBe Honest with yourself on these. Think about how confident you would be recieving a blind interview that involves using the skill.''',
    )
    class Meta:
        abstract = True












