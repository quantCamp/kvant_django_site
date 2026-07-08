from django.db import models

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(max_length=150, null=False, blank=False, default="gallery/album_placeholder.jpg",
                upload_to="gallery/")
    created_at = models.DateField(auto_now_add=True)
    #related_news = models.ForeignKey(NewsArticle, on_delete = models.SET_NULL, null = True, blank = True, related_name = "albums")
    def __str__(self):
        return self.title
    
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = "photos")
    img = models.ImageField(max_length=150, null=False, blank=False, upload_to="gallery/")
    caption = models.CharField(max_length=200, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)