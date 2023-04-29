from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Video


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "videos/index.html",
        context={
            "videos_list": Video.objects.all(),
        },
    )
