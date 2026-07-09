from django.db import models

from teachers.models import Teacher


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название курса")
    short_description = models.CharField(max_length=255, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Полное описание")
    icon = models.CharField(max_length=50, default="📚", verbose_name="Эмодзи-иконка")
    teachers = models.ManyToManyField(Teacher, related_name="courses", verbose_name="Преподаватели")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Учебный курс"
        verbose_name_plural = "Учебные курсы"
