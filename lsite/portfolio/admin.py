from django.contrib import admin
from portfolio.models import Category, Project

# Slug field is automatic. Based on title of Project.
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Project, ProjectAdmin)
