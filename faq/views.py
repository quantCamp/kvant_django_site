from django.shortcuts import render
from .models import FAQCategory

def faq_view(request):
    categories = FAQCategory.objects.prefetch_related('items').all().order_by('order', 'name')
    return render(request, 'faq/faq_list.html', {'categories': categories})
