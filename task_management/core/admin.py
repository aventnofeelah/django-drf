from django.contrib import admin
from .models import Task, Project

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
