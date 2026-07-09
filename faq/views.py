from django.shortcuts import render

from faq.models import FAQCategory

# Create your views here.

def question(request):
    categories = FAQCategory.objects.all()

    return render (request, 'faq/faq_list.html', context= {"categories": categories})







