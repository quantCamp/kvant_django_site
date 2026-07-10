from django.contrib import admin
from .models import Category, Material

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'material_type', 'link', 'file')
    list_filter = ('category', 'material_type')
    search_fields = ('title', 'description')

