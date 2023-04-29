from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "home/contact.html")
