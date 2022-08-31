from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from reviews.models import Book, Review, Contributor

from .forms import SearchForm
from .utils import average_rating


def index(request):
    return render(request, "base.html", )


#
# def book_search(request):
#     search_text = request.GET.get("search", "")
#     return render(request, "search-results.html", {"search_text": search_text})


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


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {'book': book,
                   'book_rating': book_rating,
                   'reviews': reviews}
    else:
        context = {'book': book,
                   'book_rating': None,
                   'reviews': None}
    return render(request, "reviews/book_detail.html", context)


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == 'title':
            books = Book.objects.filter(title__icontains=search)

        else:
            fname_contributors = Contributor.objects.filter(first_names__itcontains=search)
            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
            lname_contributors = Contributor.objects.filter(last_names__itcontains=search)
            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
    return render(request, "reviews/search-results.html", {"form": form, "search_text": search_text, "books": books})


class HomePage(TemplateView):
    template_name = 'home_page.html'
