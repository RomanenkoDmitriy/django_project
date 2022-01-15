from django.urls import path, include
from . import views

urlpatterns = [
    path('registration', views.registration_user, name='registration'),
]