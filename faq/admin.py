from django.contrib import admin
from .models import FAQCategory, FAQItem

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    ordering = ('order', 'name')

@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'question', 'category')
    list_filter = ('category',)
    ordering = ('category', 'order', 'question')
