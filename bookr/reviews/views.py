from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     name = request.GET.get("name") or "nieznajomy"
#     return HttpResponse("Hej, {}! Czy ja się tutaj wyświetlam?".format(name))

# def index(request):
#     name = "Świecie"
#     return render(request, "base.html", {"name": name})
from django.views.generic import TemplateView

from reviews.models import Book


def index(request):
    return render(request, "base.html", )


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-result.html", {"search_text": search_text})

def my_view(request,id):
    user = User.objects.get(id=id)
    return HttpResponse(f"ten użytkownik nazywa się {user.first_name} {user.last_name}")

def welcome_view(request):
    message = f"<html><h2>Witaj w aplikacji BookR</h2><p>W bazie jest {Book.objects.count()} książek.</p></html>"
    return HttpResponse(message)



class HomePage(TemplateView):
    template_name = 'home_page.html'

