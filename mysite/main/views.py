from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


# Create your views here.
def index(request):

    context = {
        "title": "Главная-страница",
        "content": "Магазин мебели ", 
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас", 
        "content": "О нас",
        'text_on_page': "Какой-то странный текст"
    }

    return render(request, "main/about.html", context)
