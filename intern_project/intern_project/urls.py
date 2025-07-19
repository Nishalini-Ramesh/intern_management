"""
URL configuration for intern_project project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 Include all routes from growtern app
    path('', include('growtern.urls')),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
