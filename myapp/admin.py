from django.contrib import admin
from .models import tasks

class taskadmin(admin.ModelAdmin):
    list_display=("title","description","duedate","iscompleted")
    
# Register models
admin.site.register(tasks,taskadmin)
