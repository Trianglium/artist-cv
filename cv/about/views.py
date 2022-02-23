
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Section, Entry
from .forms import EntryForm, SectionForm, ContactForm

class EntryListView(ListView):
     model = Entry
     fields = ['content', 'resume_section', 'start_date', 'end_date']
     template_name = 'about/main.html'

     def get_context_data(self, **kwargs):
         context = super(EntryListView, self).get_context_data(**kwargs)
         context.update({
             'entry_list': Entry.objects.all(),
             'section_list': Section.objects.all(),
         })
         return context

     def get_queryset(self):
         return Entry.objects.order_by('resume_section')

class SectionListView(ListView):
    model = Section
    fields = ['title']
    template_name = 'about/section_list.html'

    def get_queryset(self):
        return Section.objects.all()


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




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'about/contact.html'
    # TO DO - Create a view for 'thanks' or some other confirmation and change success_url to that
    success_url = reverse_lazy('about:all')
    # TO DO - add methods







