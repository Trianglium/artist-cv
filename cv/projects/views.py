from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from projects.models import Project

class ProjectIndexView(generic.ListView):
    model = Project
    template_name = 'projects/project_index.html'



class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
