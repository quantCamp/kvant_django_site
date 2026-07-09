from django.db import models


# Create your models here.
class ScheduleItem(models.Model):
    order = models.IntegerField(unique=True, null=False, blank=False)
    time_start = models.TimeField(null=False, blank=False)
    time_end = models.TimeField(null=True, blank=True)
    event_name = models.CharField(max_length=150, null=False, blank=False)
    short_description = models.CharField(max_length=255, null=False, blank=False)
    detailed_description = models.TextField(null=False, blank=False)
