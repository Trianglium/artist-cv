from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name = 'projects'
urlpatterns = [
    # ex: /projects/
    path('', views.ProjectIndexView.as_view(), name='all'),
    # ex: /projects/project/3/
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    # ex: /projects/project/create
    path('project/create', views.ProjectCreateView.as_view(success_url=reverse_lazy('projects:all')), name='project_create'),
    # ex: /projects/project/3/update
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(success_url=reverse_lazy('projects:all')), name='project_update'),
    # ex: /projects/project/3/delete
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(success_url=reverse_lazy('projects:all')), name='project_delete'),
    # ex: projects/content/uploads/6/
    path('content/uploads/<int:pk>/', views.stream_file, name='uploads'),
]