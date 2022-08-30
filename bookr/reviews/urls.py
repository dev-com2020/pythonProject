from django.contrib import admin
from django.urls import path, include

from reviews import views

urlpatterns = [path('', views.welcome_view, name="welcome_view"),
               ]
