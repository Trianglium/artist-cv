from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views
from portfolio.views import ProjectListView, ProjectDetailView

app_name='portfolio'
urlpatterns = [
    path('', views.IndexView, name='all'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail')
]
