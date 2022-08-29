from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     name = request.GET.get("name") or "nieznajomy"
#     return HttpResponse("Hej, {}! Czy ja się tutaj wyświetlam?".format(name))

# def index(request):
#     name = "Świecie"
#     return render(request, "base.html", {"name": name})

def index(request):
    return render(request, "base.html", )


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-result.html", {"search_text": search_text})
