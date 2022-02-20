
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views.generic.base import View

from about.models import Resume, Category

# List / Index Views of Models

# Home / Landing Page View
class HomeView(ListView):
    pass

# Resume Model (Personal Data) - ListView
class AboutView(ListView):
    queryset = Resume.objects.all()
    template_name = 'about/aboutme.html'
    context_object_name = 'resume_data'



# Category Model (Generic Resume Sections expected on all resumes)
class CategoryView(ListView):
    context_object_name = 'header_categories'
    queryset = Category.objects.all()
    template_name = 'about/category_index.html'



# Resume (Personal Data Input) - Create / Update / Delete Views
class AboutMeCreate(LoginRequiredMixin, CreateView):
    template='about/resume_form.html'
    model = Resume
    fields = '__all__'
    success_url = reverse_lazy('about:all')

class AboutMeUpdate(LoginRequiredMixin, UpdateView):
    template='about/resume_update.html'
    model = Resume
    fields = '__all__'
    success_url = reverse_lazy('about:all')

class AboutMeDelete(LoginRequiredMixin, DeleteView):
    template='about/resume_confirm_delete.html'
    model = Resume
    fields = '__all__'
    success_url = reverse_lazy('about:all')


# Section Category (Generic) - Create / Update / Delete Views
#
class CategoryCreate(LoginRequiredMixin, CreateView):
    template='autos/category_create.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('about:all')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    template='autos/category_update.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('about:all')


class CategoryDelete(LoginRequiredMixin, DeleteView):
    template='autos/category_confirm_delete.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('about:all')