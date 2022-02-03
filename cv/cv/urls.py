from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
