from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'done']
    readonly_fields = ['slug']
    list_display_links = ['title']