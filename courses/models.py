from django.db import models
# Предположим, модель Teacher находится в приложении teachers
from teachers.models import Teacher 

class Course(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Название курса")
    short_description = models.CharField(max_length=255, null=False, blank=False, verbose_name="Краткое описание")
    description = models.TextField(null=False, blank=False, verbose_name="Полное описание")
    icon = models.CharField(max_length=50, null=False, blank=False, default="📚", verbose_name="Эмодзи-иконка")
    teachers = models.ManyToManyField(Teacher, related_name="courses", verbose_name="Преподаватели")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Учебный курс"
        verbose_name = "Учебные курсы"
