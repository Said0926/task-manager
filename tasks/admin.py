from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('name', 'user__username')
    ordering = ['-created_at']
    list_display_links = ('name',)
    list_editable = ('status',)
    
admin.site.register(Task, TaskAdmin)
