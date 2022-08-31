from django.contrib import admin
from django.urls import path, include

from reviews import views

urlpatterns = [path('', views.index, name="index"),
               path('books/', views.book_list, name="book_list"),
               path('book/<int:pk>/', views.book_detail, name="book_detail"),
               path('book/<int:book_pk>/reviews/new', views.review_edit, name="review_create"),
               path('book/<int:book_pk>/reviews/<int:review_pk>', views.review_edit, name="review_edit"),
               path('book-search/', views.book_search, name="book_search"),
               path('publishers/<int:pk>/', views.publisher_edit, name="publisher_edit"),
               path('publishers/new/', views.publisher_edit, name="publisher_create"),

               ]
