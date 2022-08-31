from django.contrib import admin
from django.urls import path, include

from reviews import views

urlpatterns = [path('', views.index, name="index"),
               path('books/', views.book_list, name="book_list"),
               path('book/<int:pk>/', views.book_detail, name="book_detail"),
               ]
