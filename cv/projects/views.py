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
from projects.forms import CreateForm


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
    fields = ['title', 'description', 'skills', 'uploads', 'links']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk):
        p = Project.objects.get(id=pk)
        return render(request, template_name=self.template, context={'project':p})


# Create a New Project.
class ProjectCreateView(LoginRequiredMixin, View):
    template='projects/project_form.html'
    model = Project
    fields = ['title', 'summary', 'description', 'uploads', 'links', 'skills']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        form = CreateForm()
        return render(request, template_name=self.template, context={'form': form})

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
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
    fields = ['title','summary', 'description', 'uploads', 'links','skills']
    success_url = reverse_lazy('projects:all')

    def get(self, request, pk=None):
        project = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = CreateForm(instance=project)
        return render(request, template_name=self.template, context={'form':form})

    def post(self, request, pk=None):
        project = get_object_or_404(Project, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=project)

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
    fields = ['title','summary', 'description', 'uploads', 'links', 'skills']
    success_url = reverse_lazy('projects:all')

# Sets Content.project_content field
def stream_file(request, pk):
    content = get_object_or_404(Content, id=pk)
    response = HttpResponse()
    response['Content-Type'] = content.content_type
    response['Content-Length'] = len(content.project_content)
    response.write(content.project_content)
    return response
