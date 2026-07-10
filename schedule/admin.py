from django.contrib import admin
from .models import ScheduleItem

@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'event_name', 'time_start', 'time_end', 'short_description')
    ordering = ('order',)

