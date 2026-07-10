from django.db import models

# Create your models here.
class SchoolApplication(models.Model):
    parent_name = models.CharField(max_length=50, blank=False) # label='Имя родителя', 
    student_name = models.CharField(max_length=50, blank=False) # label='Имя учащегося', 
    student_age = models.IntegerField(blank=False) # label='Возраст учащегося', 
    phone = models.CharField(max_length=15, blank=False) # label='Номер телефона', 
    email = models.EmailField(blank=False) # label='e-mail', 
    achievements = models.ImageField(upload_to="achievements/") # label="Достижения", 