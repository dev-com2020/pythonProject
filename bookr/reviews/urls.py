from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from reviews import views

from reviews.views import IndexView

from reviews import api_views

urlpatterns = [path('', views.index, name="index"),
               path('books/', views.book_list, name="book_list"),
               path('book/<int:pk>/', views.book_detail, name="book_detail"),
               path('book/<int:pk>/media/', views.book_media, name="book_media"),
               path('book/<int:book_pk>/reviews/new', views.review_edit, name="review_create"),
               path('book/<int:book_pk>/reviews/<int:review_pk>', views.review_edit, name="review_edit"),
               path('book-search/', views.book_search, name="book_search"),
               path('publishers/<int:pk>/', views.publisher_edit, name="publisher_edit"),
               path('publishers/new/', views.publisher_edit, name="publisher_create"),
               path('books/profile', TemplateView.as_view(template_name='profile.html')),
               path('test', IndexView.as_view(), name='index_view'),
               path('api/first/', api_views.first_api_view),
               path('api/all/', api_views.all_books, name='all_books'),
               path('api/login', api_views.Login.as_view(), name='login'),


               ]
