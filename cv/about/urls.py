from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name = 'about'
urlpatterns = [
    path('resume/', views.EntryListView.as_view(), name='all'),
    path('resume/new/entry/', views.EntryCreateView.as_view(), name='new_entry'),
    path('resume/edit/entry/<int:pk>/', views.EntryUpdateView.as_view(), name='edit_entry'),
    path('resume/delete/entry/<int:pk>/', views.EntryDeleteView.as_view(), name='delete_entry'),
    path('resume/new/section/', views.SectionUpdateView.as_view(), name='new_section'),
    path('resume/edit/section/<int:pk>/', views.SectionUpdateView.as_view(), name='edit_section'),
    path('resume/delete/section/<int:pk>/', views.SectionDeleteView.as_view(), name='delete_section'),
    path('contact/', views.ContactFormView.as_view(), name='connect'),

]
