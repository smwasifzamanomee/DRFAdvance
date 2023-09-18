from django.contrib import admin
from .models import Status

# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'content', 'image']
    list_filter = ['user', 'updated']
    search_fields = ['user__username', 'user__email', 'content']
    
    class Meta:
        model = Status
        
admin.site.register(Status, StatusAdmin)