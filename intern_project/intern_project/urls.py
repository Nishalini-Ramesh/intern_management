"""
URL configuration for intern_project project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from growtern import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👇 Include all routes from growtern app
    path('', include('growtern.urls')),
    path('create-task/', views.create_task, name='create_task'),
    path('', include('growtern.urls')), 
    
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('growtern.urls')),  
]


