from django.db import models
from django.conf import settings
from base.models import Organization, Skill



class Professional(Organization):
    # Inherits all fields from Organization
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Educational(Organization):
    # Inherits all fields from Organization
    # .credential: (Optional field) Meant for credentials. IE degree, diploma, certificate, etc.
    credential = models.CharField(max_length=255, null=True)
    # .secondary_credential: minor, secondary area of focus, specialization, or -
    # other courses/certificates that are related to the main credential
    secondary_credentials = models.TextField(max_length=500, null=True)
    # .url: (Optional field) meant for certifications and other. URL to validate or URL to view the credential
    url = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.credential

class Volunteer(Organization):
    # Inherits all fields from Organization
    def __str__(self):
        return self.institution


class Technical(Skill):
    # Inherits all fields from Skill
    def __str__(self):
        return self.name

class Interpersonal(Skill):
    # Inherits all fields from Skill
    def __str__(self):
        return self.name



# ProfessionalProfile as to separate info from the User Auth Model (CVAuth) and AuthorProfile (Blog)
# Again, Allowing for a separation of concerns and added security.
class ProfessionalProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resume"
    )
    objective = models.TextField(null=True, editable=True)
    resume_summary = models.TextField(null=True, editable=True)
    public_email = models.TextField(null=True, editable=True)
    resume_link = models.TextField(null=True, editable=True, help_text="Upload your resume to Google Drive and Share the File with anyone who has the link. Copy and Paste the link into this field")

    def download_resume(self):
        link = str(self.resume_link).split('file/d')
        base = f'{link[0]}uc?export=download&id={}'

        return



    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"
