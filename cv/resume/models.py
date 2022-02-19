from django.db import models
from django.conf import settings
from base.models import Organization, Skill



class Professional(Organization):
    # Inherits all fields from Organization
    title = models.CharField(max_length=255, help_text='Job Title or Professional Title')

    class Meta:
        verbose_name = 'Professional Experience'
        verbose_name_plural = 'Professional Experience'

    def __str__(self):
        return self.title


class Educational(Organization):
    # Inherits all fields from Organization
    # .credential: (Optional field) Meant for credentials. IE degree, diploma, certificate, etc.
    credential = models.CharField(max_length=255, null=True, help_text='Enter Credentials here. Degrees, Certifications, Licenses, Diplomas, Etc.')
    # .secondary_credential: minor, secondary area of focus, specialization, or -
    # other courses/certificates that are related to the main credential
    secondary_credentials = models.TextField(max_length=500, null=True, help_text='Enter related course, certificates, or minor credentials that are related to the input above. IE a Minor in Pyschology')
    # .url: (Optional field) meant for certifications and other. URL to validate or URL to view the credential
    url = models.URLField(max_length=500, null=True, help_text='This field is meant for certifications and other credentials that offer a url to validate the credential')

    class Meta:
        verbose_name = 'Education/Certification'
        verbose_name_plural = 'Education/Certification'

    def __str__(self):
        return self.credential

class Volunteer(Organization):
    # Inherits all fields from Organization
    class Meta:
        verbose_name = 'Volunteer Experience'
        verbose_name_plural = 'Volunteer Experience'

    def __str__(self):
        return self.institution


class Technical(Skill):
    # Inherits all fields from Skill
    class Meta:
        verbose_name = 'Technical/Hard Skill'
        verbose_name_plural = 'Technical/Hard Skills'

    def __str__(self):
        return self.skill_name

class Interpersonal(Skill):
    # Inherits all fields from Skill
    class Meta:
        verbose_name = 'Interpersonal/Soft Skill'
        verbose_name_plural = 'Interpersonal/Soft Skills'

    def __str__(self):
        return self.skill_name



# ProfessionalProfile as to separate info from the User Auth Model (CVAuth) and AuthorProfile (Blog)
# Again, Allowing for a separation of concerns and added security.
class ProfessionalProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resume_profile"
    )
    objective = models.TextField(null=True, blank=True, editable=True, help_text='(Optional) Resume Objective, generally found at the top of a resume/cv.')
    resume_summary = models.TextField(null=True, blank=True, editable=True, help_text='(Optional) Resume Summary Section')
    public_email = models.CharField(max_length=250, null=True, blank=True, editable=True, help_text='(Recommended) Enter the email employers should contact you at. This will be public and can be different from the signup email if you so choose.')
    resume_link = models.TextField(null=True, blank=True, editable=True, help_text='(Recommended) Upload your resume to Google Drive and Share the File with anyone who has the link. Copy and Paste the link into this field')



    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"
