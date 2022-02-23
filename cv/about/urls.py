from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name = 'about'
urlpatterns = [
    path('', views.EntryListView.as_view(), name='all'),
    path('new/entry/', views.EntryCreateView.as_view(), name='new_entry'),
    path('edit/<int:pk>/', views.EntryUpdateView.as_view(), name='edit_entry'),
    path('delete/<int:pk>/', views.EntryDeleteView.as_view(), name='delete_entry'),
    path('new/section/', views.SectionUpdateView.as_view(), name='new_section'),
    path('edit/section/<int:pk>/', views.SectionUpdateView.as_view(), name='edit_section'),
    path('delete/section/<int:pk>/', views.SectionDeleteView.as_view(), name='delete_section'),

]
