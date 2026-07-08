from django.db import models



class NewsArticle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    img = models.ImageField(null=False, blank=False, default='news/static/img/default.jpg', upload_to='news/static/img')

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
