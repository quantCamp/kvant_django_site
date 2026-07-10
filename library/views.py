from django.shortcuts import render
from library import models


def main_page(request):
    categories = models.Category.objects.all()
    return render(request, "./library/library.html", context={"categories": categories})


def category_page(request, category_id):
    materials = models.Material.objects.filter(category=category_id)
    category_name = models.Category.objects.get(id=category_id).name
    return render(request, "./library/category.html", context={"materials": materials, "name": category_name})
