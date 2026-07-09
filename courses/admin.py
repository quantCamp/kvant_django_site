from django.contrib import admin

from courses.models import Course
from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')
    search_fields = ('first_name', 'bio')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'title', 'short_description')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'short_description', 'description')
    filter_horizontal = ('teachers',)
    fieldsets = (
        ("Основная информация", {
            'fields': ('title', 'icon')
        }),
        ("Описания курса", {
            'fields': ('short_description', 'description')
        }),
        ("Персонал", {
            'fields': ('teachers',)
        }),
    )
