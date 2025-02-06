from django.contrib import admin
from .models import Task, Project, User

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
