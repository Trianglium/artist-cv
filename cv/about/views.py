from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from about.models import Section, Contact

class AboutListView(ListView):
    model = Section
    context_object_name = 'about_sections'

class SectionDetailView(DetailView):
    model = Section
    success_url = reverse_lazy('about:all')
    fields = ['__all__']
    template_name = 'about/section_detail.html'
