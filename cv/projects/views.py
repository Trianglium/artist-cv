from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.db.models import Q

from django.core.files.uploadedfile import InMemoryUploadedFile

from projects.models import Project, Link, Content
from projects.owner import OwnerListView, OwnerCreateView, OwnerDeleteView, OwnerUpdateView, OwnerDetailView
from projects.forms import ProjectForm, LinkForm, MediaForm

import logging

logger = logging.getLogger(__name__)



# Projects index page view
class ProjectIndexView(OwnerListView):
    template = 'projects/project_index.html'
    def get(self, request):
        projects_list = Project.objects.all()
        return render(request, template_name=self.template, context={'projects_list':projects_list})


# Details of a singular Project ("Read more" takes you here)
class ProjectDetailView(OwnerDetailView):
    model = Project
    template = 'projects/project_detail.html'
    # Summary not included - Only wanted it for the preview
    fields = ['title', 'description', 'skills', 'uploads']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk):
        logger.debug("projectdetailview  GET called: request: %s with pk %s" % (request, pk))
        project = Project.objects.get(id=pk)
        return render(request, template_name=self.template, context={'project':project})


# Create a New Project.
class ProjectCreateView(LoginRequiredMixin, View):
    template='projects/project_form.html'
    model = Project
    fields = ['title', 'summary', 'description', 'uploads', 'skills']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        form = ProjectForm()
        return render(request, template_name=self.template, context={'form': form})

    def post(self, request, pk=None):
        logger.debug("projectcreateview  POST called: request: %s with pk %s" % (request, pk))
        form = ProjectForm(request.POST, request.FILES or None)
        logger.debug("projectcreateview  POST called: form: %s " % (form))

        if not form.is_valid():
            logger.debug("projectcreateview  form is NOT VALID pk(id): %s" % (pk))
            return render(request, template_name=self.template, context={'form': form})

        # Add owner to the model before saving
        # Adjust before saving
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()

        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        # Next line is reason this gets saved.
        form.save_m2m()

        return redirect(self.success_url)

# Update/Edit/Change Previously Created Project
class ProjectUpdateView(LoginRequiredMixin, View):
    template='projects/project_form.html'
    model = Project
    fields = ['title','summary', 'description', 'uploads', 'skills']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        project = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectForm(instance=project)
        return render(request, template_name=self.template, context={'form':form})

    def post(self, request, pk=None):
        project = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = ProjectForm(request.POST, request.FILES or None, instance=project)

        if not form.is_valid():
            return render(request, template_name=self.template, context={'form':form})

        project = form.save(commit=False)
        project.save()

        form.save_m2m()

        return redirect(self.success_url)

# Delete Previously Created Project
class ProjectDeleteView(OwnerDeleteView):
    template='projects/project_confirm_delete.html'
    model = Project
    fields = ['title','summary', 'description', 'uploads',  'skills']
    success_url = reverse_lazy('projects:all')



# Create a New Content.
class ContentCreateView(LoginRequiredMixin, View):
    template='projects/content_form.html'
    model = Content
    fields = [ 'media', 'name']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        form = MediaForm()
        return render(request, template_name=self.template, context={'form': form})

    def post(self, request, pk=None):
        form = MediaForm(request.POST, request.FILES or None)
        logger.debug("projectcreateview  POST called: form: %s " % (form))

        if not form.is_valid():

            return render(request, template_name=self.template, context={'form': form})

        # Add owner to the model before saving
        # Adjust before saving
        content = form.save(commit=False)
        content.save()

        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        # Next line is reason this gets saved.
        form.save_m2m()

        return redirect(self.success_url)

# Update/Edit/Change Previously Created Content
class ContentUpdateView(LoginRequiredMixin, View):
    template='projects/content_form.html'
    model = Content
    fields = ['media', 'name']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        content = get_object_or_404(Content, id=pk)
        form = MediaForm(instance=content)
        return render(request, template_name=self.template, context={'form':form})

    def post(self, request, pk=None):
        content = get_object_or_404(Content, id=pk)
        form = MediaForm(request.POST, request.FILES or None, instance=content)

        if not form.is_valid():
            return render(request, template_name=self.template, context={'form':form})

        content = form.save(commit=False)
        content.save()

        form.save_m2m()

        return redirect(self.success_url)

# Delete Previously Created Content
class ContentDeleteView(OwnerDeleteView):
    template='projects/content_confirm_delete.html'
    model = Content
    fields = ['__all__']
    success_url = reverse_lazy('projects:all')


# Sets Content.media field
def stream_file(request, pk):
    pc = get_object_or_404(Content, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pc.content_type
    response['Content-Length'] = len(pc.media)
    response.write(pc.media)
    return response