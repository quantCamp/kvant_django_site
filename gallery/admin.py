from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'cover_image']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    # Важно: поле cover_image будет отображаться автоматически

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'album', 'uploaded_at']
    search_fields = ['caption']
    list_filter = ['album']