from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views
from portfolio.views import ProjectListView, ProjectDetailView

app_name = 'projects'
urlpatterns = [
    # ex: /projects/
    path('', views.ProjectIndexView.as_view(), name='project_index'),
    # ex: /projects/3/
    path('<int:question_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
