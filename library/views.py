from django.shortcuts import render
from library import models


def main_page(request):
    categories = models.Category.objects.all()
    return render(request, "./library.html", context={"categories": categories})


def category_page(request, category):
    materials = models.Material.objects.filter(category=category)
    return render(request, "./category.html", context={"materials": materials})
