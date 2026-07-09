from django.db import models

class FAQCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Категория FAQ"
        verbose_name_plural = "Категории FAQ"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class FAQItem(models.Model):
    category = models.ForeignKey(
        FAQCategory, 
        on_delete=models.CASCADE, 
        related_name="items", 
        verbose_name="Категория"
    )
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    order = models.IntegerField(default=0, verbose_name="Порядок внутри категории")

    class Meta:
        verbose_name = "Вопрос-Ответ FAQ"
        verbose_name_plural = "Вопросы-Ответы FAQ"
        ordering = ['order', 'question']

    def __str__(self):
        return self.question