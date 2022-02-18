from django.contrib import admin
from resume.models import ProfessionalProfile, Professional, Educational, Volunteer, Technical, Interpersonal


admin.site.register(ProfessionalProfile)

admin.site.register(Professional)

admin.site.register(Educational)
admin.site.register(Volunteer)

admin.site.register(Technical)
admin.site.register(Interpersonal)


