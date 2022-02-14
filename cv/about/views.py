
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from about.models import Section, Contact

class AboutListView(ListView):
    model = Section
    context_object_name = 'about_sections'

    def get_context_data(self, request):
        self.model.objects.all()
