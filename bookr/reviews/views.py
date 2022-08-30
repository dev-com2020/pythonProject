from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from reviews.models import Book, Review
from .utils import average_rating


def index(request):
    return render(request, "base.html", )


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-result.html", {"search_text": search_text})


def my_view(request, id):
    user = User.objects.get(id=id)
    return HttpResponse(f"ten użytkownik nazywa się {user.first_name} {user.last_name}")


def welcome_view(request):
    message = f"<html><h2>Witaj w aplikacji BookR</h2><p>W bazie jest {Book.objects.count()} książek.</p></html>"
    return HttpResponse(message)


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'reviews/book_list.html', context)


class HomePage(TemplateView):
    template_name = 'home_page.html'
