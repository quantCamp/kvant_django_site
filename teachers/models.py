from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    photo = models.ImageField(null=False, blank=False, default="static/img/teachers/teacher_placeholder.png", upload_to="teachers/")
    short_info = models.CharField(max_length=250, null=False,blank=False)
    bio = models.TextField(null=False, blank=False)
    achievments = models.TextField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
