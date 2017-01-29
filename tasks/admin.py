from django.contrib import admin

from .models import Task

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'last_complete',
                    'next_repeat', 'repeat_factor', 'max_repeat_factor')
    list_display_links = ('name',)
    list_filter = ('next_repeat', 'last_complete')
    search_fields = ('name', 'description')
    class Meta:
        model = Task


admin.site.register(Task, TaskModelAdmin)
