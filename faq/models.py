from django.db import models


class FAQCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False, default=0)


class FAQItem(models.Model):
    category = models.ForeignKey(
        FAQCategory,
        on_delete=models.CASCADE,
        related_name="items")
    question = models.CharField(max_length=255, null=False, blank=False)
    answer = models.TextField( null=False, blank=False)