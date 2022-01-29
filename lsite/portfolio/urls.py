from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name='portfolio'
urlpatterns = [
    path('', index.IndexView.as_view(), name='all')

]
