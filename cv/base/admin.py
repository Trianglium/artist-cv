from django.contrib import admin
from base.models import BaseAutoDate, BaseArticle, BaseContent, BaseLink

admin.site.register(BaseAutoDate)
admin.site.register(BaseContent)
admin.site.register(BaseArticle)
admin.site.register(BaseLink)