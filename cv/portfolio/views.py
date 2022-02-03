from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from portfolio.models import Project

class ProjectListView(ListView):
    model = Project
    template='portfolio/project-list.html'
    fields= '__all__'
    def get(self, request):
        projects = Project.objects.all()
        return render(request, template_name=self.template, context={'projects':projects})

class ProjectDetailView(DetailView):
    model = Project
    template_name='portfolio/project-detail.html'
    fields= '__all__'
# Displays Post Detail View ("Read More")

def post_detail(request, slug):
    # Returns the Post Content field
    post = get_object_or_404(Post, slug=slug)
def IndexView(request):
    return render(request, 'portfolio/project-index.html')
