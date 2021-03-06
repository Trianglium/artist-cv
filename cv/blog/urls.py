from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='all'),
    path('post/<slug>/', views.post_detail, name='post_detail'),
]