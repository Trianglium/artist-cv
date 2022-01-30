from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
