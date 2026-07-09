from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    material_type = models.CharField(max_length=20, null=False, blank=False,
                                     choices=[('link', 'Ссылка'), ('file', 'Файл')],
                                     default='link')
    link = models.TextField(null=True, blank=True)
    file = models.FileField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="materials")
