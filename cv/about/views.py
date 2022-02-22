
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Section, Entry

class EntryListView(ListView):
     model = Entry
     fields = ['content', 'resume_section', 'start_date', 'end_date']
     template_name = 'about/main.html'

     def get_queryset(self):
         return Entry.objects.order_by('resume_section')



class SectionCreateView(CreateView, LoginRequiredMixin):
    model = Section
    fields = ['title']
    template_name = 'about/section_form.html'
    success_url = reverse_lazy('about:all')


class SectionUpdateView(UpdateView, LoginRequiredMixin):
    model = Section
    fields = ['title']
    template_name = 'about/section_form.html'
    success_url = reverse_lazy('about:all')

class SectionDeleteView(DeleteView, LoginRequiredMixin):
    model = Section
    fields = ['title']
    template_name = 'about/section_confirm_delete.html'
    success_url = reverse_lazy('about:all')


class EntryCreateView(CreateView, LoginRequiredMixin):
     model = Entry
     fields = ['content', 'resume_section', 'start_date', 'end_date']
     template_name = 'about/entry_form.html'
     success_url = reverse_lazy('about:all')
     success_url = reverse_lazy('about:all')

class EntryUpdateView(UpdateView, LoginRequiredMixin):
     model = Entry
     fields = ['content', 'resume_section', 'start_date', 'end_date']
     template_name = 'about/entry_form.html'
     success_url = reverse_lazy('about:all')

class EntryDeleteView(DeleteView, LoginRequiredMixin):
    model = Entry
    fields = ['content', 'resume_section', 'start_date', 'end_date']
    template_name = 'about/entry_confirm_delete.html'
    success_url = reverse_lazy('about:all')