from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    #path('resume/', include('resume.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor_uploader/', include('ckeditor_uploader.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
