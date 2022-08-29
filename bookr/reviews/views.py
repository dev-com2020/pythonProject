from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = request.GET.get("name") or "nieznajomy"
    return HttpResponse("Hej, {}! Czy ja się tutaj wyświetlam?".format(name))
