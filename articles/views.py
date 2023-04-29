from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Article


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "articles/index.html",
        context={
            "articles_list": Article.objects.all(),
        },
    )
