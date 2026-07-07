from django.shortcuts import render
from library import models


def main_page(request):
    categories = models.Category.objects.all()
    return render(request, "./library.html", context=categories)
