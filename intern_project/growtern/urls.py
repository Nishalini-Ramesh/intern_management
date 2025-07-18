# growtern/urls.py

from django.urls import path
from . import views  # Make sure you have at least one view

urlpatterns = [
    path('feedback/', views.feedback_form, name='submit_feedback'),
    path('rating/', views.rating_view, name='rating'),
    path('rating/thankyou.html', views.thank_you, name='thank_you'),
]